#!/usr/bin/env python3
"""Regression checks for artifacts and helpers; not a Desktop integration test."""
from __future__ import annotations
import copy
import hashlib
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from onboarding_form import load_form, render
from check_demo import calculate_total, check_email
BASELINES = json.loads((ROOT / 'tests/expected-hashes.json').read_text(encoding='utf-8'))


def text(name: str) -> str:
    return (ROOT / name).read_text(encoding='utf-8')


def data(name: str) -> dict:
    return json.loads(text(name))


class PackageChecks(unittest.TestCase):
    def test_entrypoints(self):
        for name in ('START.md','SKILL.md','AGENTS.md','INSTRUKCJA-KLIENTA.md','VERSION'):
            self.assertTrue((ROOT / name).is_file(), name)
        self.assertEqual(text('VERSION').strip(), '1.4.0')

    def test_one_skill(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md')], ['SKILL.md'])

    def test_sample_unchanged(self):
        self.assertEqual(hashlib.sha256((ROOT / 'references/master-sample.md').read_bytes()).hexdigest(), BASELINES['master_sample'])

    def test_authorized_core_hash(self):
        self.assertNotEqual(BASELINES['master_brain'], BASELINES['previous_master_brain'])
        self.assertEqual(hashlib.sha256((ROOT / 'references/master-brain.md').read_bytes()).hexdigest(), BASELINES['master_brain'])

    def test_frozen_questionnaire(self):
        self.assertEqual(hashlib.sha256((ROOT / 'assets/onboarding-questions.json').read_bytes()).hexdigest(), BASELINES['onboarding_form'])
        form = load_form()
        self.assertEqual([q['id'] for q in form['questions']], [f'Q{i:02}' for i in range(1, 17)])
        self.assertEqual([s['id'] for s in form['sections']], ['A', 'B', 'C', 'D'])

    def test_fixed_choices(self):
        qs = {q['id']:q for q in load_form()['questions']}
        for key, count in [('Q11',4),('Q12',3),('Q13',3),('Q16',5)]:
            self.assertEqual(qs[key]['type'], 'single_choice')
            self.assertEqual([o['id'] for o in qs[key]['options']], [chr(65+i) for i in range(count)])
        self.assertEqual(qs['Q15']['section'], 'D')

    def test_no_financial_or_core_configuration_questions(self):
        questions = '\n'.join(q['text'] for q in load_form()['questions']).lower()
        for forbidden in ('vat','brutto','netto','kilometr','nocleg','180','250','markdown','liczba znak','d\u0142ugo\u015b\u0107 mail'):
            self.assertNotIn(forbidden, questions)
        self.assertIn('nie podawaj ceny', questions)

    def test_renderer_exact_questions_and_no_fake_controls(self):
        output = render()
        for q in load_form()['questions']:
            self.assertEqual(output.count(q['text']), 1)
        self.assertNotIn('[ ]', output)
        self.assertNotIn('[Prze', output)
        with self.assertRaises(ValueError):
            render('unknown')

    def test_renderer_sections_and_fresh_process(self):
        form = load_form()
        for group in form['sections']:
            output = render(group['id'])
            for q in form['questions']:
                self.assertEqual(q['text'] in output, q['section'] == group['id'])
        result = subprocess.run([sys.executable, str(ROOT/'scripts/onboarding_form.py'), '--section','A'], capture_output=True, text=True, encoding='utf-8', check=True)
        self.assertEqual(result.stdout, render('A'))

    def test_links(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' not in target and not target.startswith(('#','mailto:')):
                    self.assertTrue((path.parent / target.split('#')[0]).is_file(), (str(path), target))

    def test_no_private_profiles(self):
        private = {'company-profile.md','user-style.md','company-profile.txt','user-style.txt','profile-history.md'}
        for path in ROOT.rglob('*'):
            if path.is_file() and path.parent.name != 'references':
                self.assertNotIn(path.name, private)
        for name in ('profil','backups'):
            self.assertFalse((ROOT/name).exists())

    def test_templates(self):
        for path in (ROOT/'assets').glob('*.template.txt'):
            value = path.read_text(encoding='utf-8')
            for required in ('approval: TEMPLATE','revision: 0','schema_version: 2','tool_version: 1.4.0'):
                self.assertIn(required, value)
            for forbidden in ('VAT','brutto','netto','kilometr','180','250','70-130','Markdown','Cena podstawowa:','Orientacyjny cennik:','Dojazd / nocleg','Domy\u015blne planowane za\u0142\u0105czniki:'):
                self.assertNotIn(forbidden, value)

    def test_separate_catalogs(self):
        value = text('assets/company-profile.template.txt')
        for q in ('Q06','Q07','Q08'):
            self.assertIn(q, value)
        self.assertNotIn('Q11', value)
        self.assertNotIn('Q16', value)

    def test_style_separated(self):
        value = text('assets/user-style.template.txt')
        for q in ('Q11','Q12','Q13','Q14','Q16'):
            self.assertIn(q, value)
        for q in ('Q01','Q06','Q07','Q08'):
            self.assertNotIn(q, value)

    def test_signature(self):
        value = text('references/signature.md')
        for q in ('Q16','Q15','Q01','Q02'):
            self.assertIn(q, value)
        self.assertEqual(sorted(re.findall(r'^([1-4])\.',value,re.M)), ['1','2','3','4'])

    def test_ignore(self):
        value = text('.gitignore')
        for required in ('/profil/','**/user-style.md','!/references/company-profile.md','.env'):
            self.assertIn(required, value)

    def test_utf8_and_no_private_recordings(self):
        for path in ROOT.rglob('*'):
            if path.is_file() and path.suffix in ('.md','.txt','.json','.yaml'):
                value = path.read_text(encoding='utf-8')
                self.assertNotIn('\ufffd', value, str(path))
                self.assertNotIn('fathom.video/share/', value, str(path))
                self.assertIsNone(re.search(r'~[acelnoszxACELNOSZX]', value), str(path))

    def test_persistence_and_migration(self):
        local = text('references/local-workspace.md')
        for required in ('ROOT/profil/company-profile.md','ROOT/profil/user-style.md','company_key','revision','backups','Ponownie odczytaj'):
            self.assertIn(required, local)
        profile = text('references/company-profile.md')
        for required in ('Migracja','kopie','Nie uruchamiaj automatycznie wszystkich 16'):
            self.assertIn(required, profile)

    def test_no_visible_technical_finish(self):
        value = text('references/onboarding.md')
        self.assertIn('Nie pokazuj', value)
        self.assertIn('kart plik', value)
        self.assertIn('AUTOMATYCZNIE', value)
        guide = text('INSTRUKCJA-KLIENTA.md')
        self.assertNotIn('rewizj', guide)
        self.assertNotIn('ROOT/', guide)
        self.assertNotIn('company-profile', guide)

    def test_demo_isolation_and_unknown_date(self):
        scenario = data('assets/demo-offer.json')
        self.assertTrue(scenario['is_demo'])
        self.assertTrue(scenario['never_persist_to_company_or_style'])
        self.assertIsNone(scenario['couple']['date'])
        self.assertIsNone(scenario['service']['headcount'])
        self.assertEqual(scenario['attachments'], [])
        value = text('references/demo-workflow.md')
        self.assertIn('Nigdy nie zapisuj', value)
        self.assertIn('Inne bran', value)

    def test_demo_amounts(self):
        scenario = data('assets/demo-offer.json')
        self.assertEqual(scenario['service']['price'],6500)
        self.assertEqual(scenario['travel']['price'],500)
        self.assertEqual([x['price'] for x in scenario['selected_extras']],[600,300])
        self.assertEqual(calculate_total(scenario),7900)
        self.assertEqual(hashlib.sha256((ROOT/'assets/demo-offer.json').read_bytes()).hexdigest(), BASELINES['demo_scenario'])

    def test_demo_rejects_changed_total_or_lodging(self):
        for mutate in ('total','lodging','flag'):
            s=copy.deepcopy(data('assets/demo-offer.json'))
            if mutate=='total': s['total_payable']=7600
            elif mutate=='lodging': s['lodging']['price']=0
            else: s['is_demo']=False
            with self.assertRaises(ValueError): calculate_total(s)

    def test_demo_email_fixture(self):
        email = data('tests/fixtures/demo-output.json')
        self.assertTrue(email['fictional_fixture'])
        self.assertEqual(check_email(email), [])

    def test_demo_email_negative_format_and_cta(self):
        email = data('tests/fixtures/demo-output.json')
        bad=copy.deepcopy(email); bad['body']+=' \u2014 **test**'
        self.assertTrue(check_email(bad))
        bad=copy.deepcopy(email); bad['body']=bad['body'].replace('jutro o 18:00','za tydzie\u0144')
        self.assertTrue(any('CTA' in e for e in check_email(bad)))
        bad=copy.deepcopy(email); bad['body']=bad['body'].replace('7 900','7 000')
        self.assertTrue(any('7900' in e for e in check_email(bad)))

    def test_metadata(self):
        value=text('agents/openai.yaml')
        self.assertIn('display_name:',value)
        self.assertIn('short_description:',value)


if __name__ == '__main__':
    unittest.main(verbosity=2)
