#!/usr/bin/env python3
"""Render the stable common onboarding and selected service modules."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def load_core() -> dict:
    form = json.loads((ROOT / 'assets/onboarding-questions.json').read_text(encoding='utf-8'))
    ids = [q['id'] for q in form['questions']]
    if ids != ['Q01','Q02','Q03','Q09','Q10','Q11','Q12','Q13','Q14','Q15','Q16']:
        raise ValueError('Unexpected common question IDs')
    return form


def load_modules() -> dict:
    data = json.loads((ROOT / 'assets/service-modules.json').read_text(encoding='utf-8'))
    expected = {'dj','photography','video','music','universal'}
    if set(data['modules']) != expected:
        raise ValueError('Unexpected service modules')
    for key, module in data['modules'].items():
        fields = [q['field'] for q in module['questions']]
        if fields != ['scope','delivery_team','extras','related_services']:
            raise ValueError(f'Invalid logical fields in {key}')
    return data


def render_core(section: str = 'all') -> str:
    form = load_core()
    allowed = {'all'} | {s['id'] for s in form['sections']}
    if section not in allowed:
        raise ValueError('Unknown section')
    lines=[]
    for group in form['sections']:
        if section != 'all' and group['id'] != section:
            continue
        lines.append(group['title'])
        for q in form['questions']:
            if q['section'] != group['id']:
                continue
            lines += ['', f"{q['id']}. {q['text']}"]
            for o in q.get('options',[]):
                lines.append(f"{o['id']}. {o['label']}")
        lines.append('')
    return '\n'.join(lines).strip()+'\n'


def render_module(name: str) -> str:
    data=load_modules(); module=data['modules'][name]
    lines=[module['label']]
    for q in module['questions']:
        lines += ['', f"{q['id']}. {q['text']}"]
    return '\n'.join(lines).strip()+'\n'


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--section', default='all', choices=['all','A','C','D'])
    p.add_argument('--module', choices=['dj','photography','video','music','universal'])
    args=p.parse_args()
    try:
        print(render_module(args.module) if args.module else render_core(args.section), end='')
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f'Cannot render onboarding: {e}', file=sys.stderr); return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
