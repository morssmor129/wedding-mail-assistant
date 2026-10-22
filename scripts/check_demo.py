#!/usr/bin/env python3
"""Check demo arithmetic and an optional email JSON. Not an integration test."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def calculate_total(scenario: dict) -> int:
    if scenario.get('is_demo') is not True or scenario.get('approved_for_demo') is not True:
        raise ValueError('Not an approved demonstration scenario')
    costs = [scenario['service']['price'], scenario['travel']['price']]
    costs.extend(item['price'] for item in scenario['selected_extras'])
    if any(type(value) is not int or value < 0 for value in costs):
        raise ValueError('Expected nonnegative whole PLN amounts')
    lodging = scenario['lodging']
    if lodging != {'provided_by': 'client', 'nights': 2, 'price': None, 'included_in_total': False}:
        raise ValueError('Lodging must remain separate, unpriced, for two nights')
    total = sum(costs)
    if total != scenario['total_payable'] or total != 7900:
        raise ValueError('Incorrect demo total')
    if scenario['attachments'] or not scenario['never_persist_to_company_or_style']:
        raise ValueError('Demo must have no attachments and must not change profiles')
    return total


def check_email(email: dict) -> list[str]:
    errors: list[str] = []
    body = email.get('body', '')
    if not isinstance(body, str) or not body.strip():
        return ['Missing email body']
    signature = email.get('signature', [])
    if not isinstance(signature, list) or len(signature) not in (3, 4):
        errors.append('Signature must contain closing, full name, company and optional confirmed link')
    if not email.get('subject'):
        errors.append('Missing subject')
    word_count = len(body.split())
    if not 180 <= word_count <= 250:
        errors.append(f'Body word count outside the product range: {word_count}')
    combined = body + '\n' + '\n'.join(str(x) for x in signature)
    if '\u2013' in combined or '\u2014' in combined:
        errors.append('Long dashes are not allowed')
    if re.search(r'\*\*|```|^\s*#{1,6}\s|^\s*[-*+]\s|<\s*[A-Za-z][^>]*>', combined, re.M):
        errors.append('Markdown or HTML detected')
    for value in ['6500', '500', '600', '300', '7900']:
        pattern = r'(?<!\d)' + r'[ \u00a0\u202f]*'.join(value) + r'(?!\d)'
        if not re.search(pattern, body):
            errors.append(f'Missing confirmed amount: {value}')
    lower = body.lower()
    if not re.search(r'jutro.*18(?::00|\.00)?', lower):
        errors.append('Missing tomorrow 18:00 CTA')
    if 'nocleg' not in lower or not re.search(r'dwie doby|2 doby|dwie noce|2 noce', lower):
        errors.append('Missing lodging for two nights')
    if 'w za\u0142\u0105cz' in lower:
        errors.append('Demo does not include attachments')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--email', type=Path, help='JSON with subject, body, and signature list')
    args = parser.parse_args()
    try:
        scenario = json.loads((ROOT / 'assets/demo-offer.json').read_text(encoding='utf-8'))
        total = calculate_total(scenario)
        errors = check_email(json.loads(args.email.read_text(encoding='utf-8'))) if args.email else []
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f'Demo validation failed: {error}', file=sys.stderr)
        return 1
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Demo checks passed; total {total} PLN; lodging separate. No Desktop integration tested.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
