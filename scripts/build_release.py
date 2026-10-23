#!/usr/bin/env python3
"""Publisher-only: generate the stable manifest from explicitly Git-tracked files.

Run after staging publisher files. Customer profiles must never be tracked.
This script does not create a GitHub release, push, schedule or install anything.
"""
from pathlib import Path
import hashlib
import json
import subprocess
from update_guard import REPO, managed, safe, version


def build(root: Path) -> dict:
    value = (root / 'VERSION').read_text(encoding='utf-8').strip()
    version(value)
    tracked = subprocess.check_output(['git', '-C', str(root), 'ls-files', '-z']).decode('utf-8').split('\0')
    files = {}
    for name in sorted(filter(None, tracked)):
        if name == 'release.json':
            continue
        if not managed(name):
            raise ValueError('Unmanaged/private tracked file: ' + name)
        files[name] = hashlib.sha256(safe(root, name).read_bytes()).hexdigest()
    result = {'schema_version': 1, 'repository': REPO, 'channel': 'stable',
              'version': value, 'files': files}
    (root / 'release.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return result


if __name__ == '__main__':
    result = build(Path(__file__).resolve().parents[1])
    print('Prepared stable release', result['version'], 'with', len(result['files']), 'managed files')
