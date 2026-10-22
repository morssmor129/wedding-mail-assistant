#!/usr/bin/env python3
"""Render the canonical onboarding without paraphrasing or inventing controls."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def load_form(path: Path | None = None) -> dict:
    path = path or ROOT / 'assets/onboarding-questions.json'
    form = json.loads(path.read_text(encoding='utf-8'))
    if [q['id'] for q in form['questions']] != [f'Q{i:02d}' for i in range(1, 17)]:
        raise ValueError('Expected the ordered canonical questions Q01-Q16')
    sections = {s['id'] for s in form['sections']}
    if sections != {'A', 'B', 'C', 'D'}:
        raise ValueError('Expected four canonical sections')
    for question in form['questions']:
        if question['section'] not in sections or not question.get('text'):
            raise ValueError('Invalid question')
        if question['type'] == 'single_choice' and not question.get('options'):
            raise ValueError('Choice question requires options')
    return form


def render(section: str = 'all', form: dict | None = None) -> str:
    form = form or load_form()
    if section not in ('all', 'A', 'B', 'C', 'D'):
        raise ValueError('Unknown section')
    lines: list[str] = []
    for group in form['sections']:
        if section != 'all' and group['id'] != section:
            continue
        lines.append(group['title'])
        for q in form['questions']:
            if q['section'] != group['id']:
                continue
            lines.extend(('', f"{int(q['id'][1:])}. {q['text']}"))
            for option in q.get('options', []):
                lines.append(f"{option['id']}. {option['label']}")
        lines.append('')
    return '\n'.join(lines).strip() + '\n'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--section', choices=['all', 'A', 'B', 'C', 'D'], default='all')
    args = parser.parse_args()
    try:
        print(render(args.section), end='')
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f'Cannot render onboarding: {error}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
