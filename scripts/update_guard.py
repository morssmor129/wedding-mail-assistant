#!/usr/bin/env python3
"""Validate a staged WMA release; update managed files only after explicit consent.

No network, no scheduler, no shell execution. An agent retrieves a pinned release
from the authorized publisher and passes that staged directory to this helper.
SHA-256 verifies consistency, not publisher identity. Never trust a random archive.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import tempfile
import uuid

REPO = 'morssmor129/wedding-mail-assistant'
ROOT_FILES = {'SKILL.md', 'START.md', 'AGENTS.md', 'README.md', 'INSTRUKCJA-KLIENTA.md',
              'CHANGELOG.md', 'QA-REPORT.md', 'VERSION', '.gitignore'}
DIRS = {'references', 'assets', 'scripts', 'tests', 'agents'}
PRIVATE = {'company-profile.md', 'user-style.md', 'company-profile.txt', 'user-style.txt',
           'profile-history.md', '.env'}
BLOCKED = {'profil', 'profiles', 'backups', '.git', '.wma-updates', '__pycache__'}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def version(value: str) -> tuple[int, int, int]:
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)', value):
        raise ValueError('Only stable numeric MAJOR.MINOR.PATCH versions are accepted')
    return tuple(int(p) for p in value.split('.'))


def managed(name: str) -> bool:
    p = PurePosixPath(name)
    if (not name or '\\' in name or ':' in name or p.is_absolute()
            or p.as_posix() != name or any(x in ('.', '..', '') for x in name.split('/'))):
        return False
    parts = p.parts
    if any(x.lower() in BLOCKED for x in parts):
        return False
    if p.name.lower() in PRIVATE and name != 'references/company-profile.md':
        return False
    if len(parts) == 1:
        return name in ROOT_FILES
    return (parts[0] in DIRS and not any(x.startswith('.') for x in parts)
            and p.suffix in {'.md', '.txt', '.json', '.py', '.yaml', '.yml'})


def safe(root: Path, name: str = '') -> Path:
    root = root.absolute()
    p = root / name
    for item in (p, *p.parents):
        if item.is_symlink() or (hasattr(item, 'is_junction') and item.is_junction()):
            raise ValueError('Symbolic links or junctions are not allowed')
    if not p.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escapes the tool directory')
    return p


def load_manifest(root: Path, verify: bool = True) -> dict:
    value = json.loads(safe(root, 'release.json').read_text(encoding='utf-8'))
    if value.get('schema_version') != 1 or value.get('repository') != REPO or value.get('channel') != 'stable':
        raise ValueError('Unexpected release identity or channel')
    version(value['version'])
    files = value['files']
    if not isinstance(files, dict) or not {'VERSION', 'SKILL.md', 'START.md'} <= files.keys():
        raise ValueError('Incomplete release manifest')
    for name, sha in files.items():
        if not managed(name) or not isinstance(sha, str) or not re.fullmatch(r'[a-f0-9]{64}', sha):
            raise ValueError('Unsafe manifest entry: ' + str(name))
        if verify and digest(safe(root, name).read_bytes()) != sha:
            raise ValueError('Release hash mismatch: ' + name)
    if verify and safe(root, 'VERSION').read_text(encoding='utf-8').strip() != value['version']:
        raise ValueError('VERSION and release manifest disagree')
    return value


def plan(tool: Path, candidate: Path) -> dict:
    safe(tool); safe(candidate)
    release = load_manifest(candidate)
    current = safe(tool, 'VERSION').read_text(encoding='utf-8').strip()
    if version(release['version']) <= version(current):
        raise ValueError('The staged release is not newer than the installed release')
    baseline = None
    if safe(tool, 'release.json').is_file():
        baseline = load_manifest(tool, verify=False)
        if baseline['version'] != current:
            raise ValueError('Installed VERSION and manifest disagree')
    changes = []
    for name in sorted([*release['files'], 'release.json']):
        target = safe(tool, name)
        before = digest(target.read_bytes()) if target.exists() else None
        after = digest(safe(candidate, name).read_bytes())
        if before == after:
            continue
        expected = baseline['files'].get(name) if baseline else None
        local_change = (name != 'release.json' and before is not None
                        and (expected is None or before != expected))
        changes.append({'path': name, 'before': before, 'after': after,
                        'local_change': local_change})
    result = {'from_version': current, 'to_version': release['version'],
              'tool': str(tool.resolve()), 'changes': changes,
              'local_changes': [c['path'] for c in changes if c['local_change']]}
    result['plan_id'] = digest(json.dumps(result, sort_keys=True).encode('utf-8'))
    return result


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.wma-tmp-', dir=str(path.parent))
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(content)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def apply(tool: Path, candidate: Path, approved_plan: str, approved_version: str,
          overwrite_local: bool = False) -> dict:
    prepared = plan(tool, candidate)
    if approved_plan != prepared['plan_id'] or approved_version != prepared['to_version']:
        raise ValueError('Explicit consent must match the current plan and target version')
    if prepared['local_changes'] and not overwrite_local:
        raise ValueError('Local edits require an explicit overwrite warning and consent')
    state_dir = safe(tool, '.wma-updates')
    state_dir.mkdir(exist_ok=True)
    lock = safe(tool, '.wma-updates/apply.lock')
    # An existing lock is not removed automatically, including after a crash.
    with lock.open('x', encoding='utf-8') as stream:
        stream.write(prepared['plan_id'])
    changed = []
    originals = {}
    backup = safe(tool, '.wma-updates/backups/' + uuid.uuid4().hex)
    try:
        if plan(tool, candidate)['plan_id'] != approved_plan:
            raise ValueError('Files changed after consent; obtain a new confirmation')
        payload = {c['path']: safe(candidate, c['path']).read_bytes() for c in prepared['changes']}
        for c in prepared['changes']:
            if digest(payload[c['path']]) != c['after']:
                raise ValueError('Candidate changed during preparation')
            target = safe(tool, c['path'])
            originals[c['path']] = target.read_bytes() if target.exists() else None
        backup.mkdir(parents=True, exist_ok=False)
        atomic_write(backup / 'plan.json', json.dumps(prepared, indent=2).encode('utf-8'))
        for name, content in originals.items():
            if content is not None:
                atomic_write(safe(backup, name), content)
        for c in prepared['changes']:
            name = c['path']
            target = safe(tool, name)
            actual = digest(target.read_bytes()) if target.exists() else None
            if actual != c['before']:
                raise ValueError('Concurrent local change: ' + name)
            atomic_write(target, payload[name])
            changed.append(name)
        load_manifest(tool)
    except Exception:
        for name in reversed(changed):
            target = safe(tool, name)
            if originals[name] is None:
                target.unlink(missing_ok=True)
            else:
                atomic_write(target, originals[name])
        raise
    finally:
        lock.unlink(missing_ok=True)
    return {'updated': True, 'version': prepared['to_version'], 'backup': str(backup)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['plan', 'apply'])
    parser.add_argument('--tool', required=True, type=Path)
    parser.add_argument('--candidate', required=True, type=Path)
    parser.add_argument('--approved-plan', default='')
    parser.add_argument('--approved-version', default='')
    parser.add_argument('--allow-local-overwrite', action='store_true')
    args = parser.parse_args()
    try:
        output = (plan(args.tool, args.candidate) if args.action == 'plan' else
                  apply(args.tool, args.candidate, args.approved_plan,
                        args.approved_version, args.allow_local_overwrite))
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, 'Update stopped: ' + str(error) + '\n')


if __name__ == '__main__':
    main()
