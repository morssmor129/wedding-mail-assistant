#!/usr/bin/env python3
"""Validate all fictional demo scenarios. Not an integration test."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def scenarios() -> dict:
    return json.loads((ROOT / 'assets/demo-scenarios.json').read_text(encoding='utf-8'))['scenarios']


def calculate_total(scenario: dict) -> int:
    if scenario.get('is_demo') is not True or scenario.get('approved_for_demo') is not True:
        raise ValueError('Not an approved demo')
    if scenario.get('never_persist_to_company_or_style') is not True:
        raise ValueError('Demo may not persist')
    prices = [x['price'] for x in scenario['service_lines']] + [scenario['travel']['price']]
    if any(type(v) is not int or v < 0 for v in prices):
        raise ValueError('Invalid PLN amount')
    lodging = scenario['lodging']
    if lodging.get('price') is not None or lodging.get('included_in_total') is not False:
        raise ValueError('Unpriced lodging must stay outside total')
    if scenario.get('attachments') != []:
        raise ValueError('Demo must have no attachments')
    total = sum(prices)
    if total != scenario['total_payable']:
        raise ValueError('Incorrect demo total')
    if 'jutro o 18:00' not in scenario.get('cta',''):
        raise ValueError('Missing fixed demo CTA')
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scenario', choices=list(scenarios()) + ['all'], default='all')
    args = parser.parse_args()
    try:
        selected = scenarios()
        if args.scenario != 'all':
            selected = {args.scenario: selected[args.scenario]}
        totals = {key: calculate_total(value) for key, value in selected.items()}
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f'Demo validation failed: {error}', file=sys.stderr)
        return 1
    print('Demo checks passed:', ', '.join(f'{k}={v} PLN' for k,v in totals.items()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
