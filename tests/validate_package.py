#!/usr/bin/env python3
"""Regression checks for WMA 1.5.1 artifacts; not a Desktop integration test."""
from __future__ import annotations
import hashlib
import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import update_guard as guard
from onboarding_form import load_core, load_modules
from check_demo import scenarios, calculate_total

BASE = json.loads((ROOT/'tests/expected-hashes.json').read_text(encoding='utf-8'))


def text(path: str) -> str:
    return (ROOT/path).read_text(encoding='utf-8')


def data(path: str) -> dict:
    return json.loads(text(path))


class PackageChecks(unittest.TestCase):
    def test_version_consistency(self):
        self.assertEqual(text('VERSION').strip(), '1.5.1')
        for path in ('README.md','SKILL.md','START.md','QA-REPORT.md'):
            self.assertIn('1.5.1', text(path), path)
        for path in ('assets/company-profile.template.txt','assets/user-style.template.txt'):
            self.assertIn('tool_version: 1.5.1', text(path), path)
        self.assertIn('tool_version to 1.5.1', text('references/local-workspace.md'))

    def test_one_skill_and_metadata(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md')], ['SKILL.md'])
        meta=text('agents/openai.yaml')
        self.assertIn('display_name:', meta)
        self.assertIn('short_description:', meta)

    def test_master_sample_and_brain_unchanged(self):
        self.assertEqual(hashlib.sha256((ROOT/'references/master-sample.md').read_bytes()).hexdigest(), BASE['master_sample'])
        self.assertEqual(hashlib.sha256((ROOT/'references/master-brain.md').read_bytes()).hexdigest(), BASE['master_brain'])

    def test_modular_onboarding_hashes(self):
        self.assertEqual(hashlib.sha256((ROOT/'assets/onboarding-questions.json').read_bytes()).hexdigest(), BASE['onboarding_core'])
        self.assertEqual(hashlib.sha256((ROOT/'assets/service-modules.json').read_bytes()).hexdigest(), BASE['service_modules'])
        core=load_core()
        self.assertEqual([q['id'] for q in core['questions']], ['Q01','Q02','Q03','Q09','Q10','Q11','Q12','Q13','Q14','Q15','Q16'])
        self.assertEqual([s['id'] for s in core['sections']], ['A','C','D'])
        q1=core['questions'][0]['text'].lower()
        self.assertIn('wszystkie usługi', q1)
        self.assertIn('zespole', q1)

    def test_modules_and_logical_fields(self):
        modules=load_modules()['modules']
        self.assertEqual(set(modules), {'dj','photography','video','music','universal'})
        for key, module in modules.items():
            self.assertEqual([q['field'] for q in module['questions']], ['scope','delivery_team','extras','related_services'], key)
        photo=' '.join(q['text'].lower() for q in modules['photography']['questions'])
        music=' '.join(q['text'].lower() for q in modules['music']['questions'])
        self.assertNotIn('saksofonist', photo)
        self.assertNotIn('album', music)

    def test_company_profile_schema_and_style_separation(self):
        company=text('assets/company-profile.template.txt')
        style=text('assets/user-style.template.txt')
        for required in ('schema_version: 3','tool_version: 1.5.1','approval: TEMPLATE','Usługi sprzedawane klientom'):
            self.assertIn(required, company)
        for required in ('schema_version: 3','tool_version: 1.5.1','Q11','Q12','Q13','Q14','Q16'):
            self.assertIn(required, style)
        for forbidden in ('Q11','Q12','Q13','Q14','Q16'):
            self.assertNotIn(forbidden, company)

    def test_source_analysis_boundaries(self):
        value=text('references/source-analysis.md').lower()
        for required in ('pdf','docx','strony www','instagram','facebook','konflikt','wcześniejszy mail'):
            self.assertIn(required, value)
        self.assertIn('nie analizuj automatycznie instagrama', value)
        self.assertIn('nie przenoś ceny podstawowej', value)

    def test_multi_service_offer_rules(self):
        value=text('references/offer-workflow.md').lower()
        self.assertIn('firmy wielousługowej', value)
        self.assertIn('pakiecie łączonym', value)
        self.assertIn('nie sumuj automatycznie', value)
        self.assertIn('pdf-u, www lub fathoma nie zastępują potwierdzenia', value)

    def test_signature_rule_present(self):
        value=text('references/signature.md')
        for q in ('Q16','Q15','Q01','Q02'):
            self.assertIn(q, value)

    def test_demos_all_valid_and_isolated(self):
        self.assertEqual(hashlib.sha256((ROOT/'assets/demo-scenarios.json').read_bytes()).hexdigest(), BASE['demo_scenarios'])
        values=scenarios()
        self.assertEqual(set(values), {'dj','photography','video','music','combined','universal'})
        for key, scenario in values.items():
            self.assertGreater(calculate_total(scenario),0,key)
            self.assertTrue(scenario['never_persist_to_company_or_style'])
        self.assertIn('Nigdy nie zapisuj danych demo', text('references/demo-workflow.md'))

    def test_update_policy_and_profiles_protected(self):
        task=data('assets/update-task.json')
        self.assertFalse(task['auto_install'])
        self.assertTrue(task['require_user_consent_for_each_update'])
        updates=text('references/updates.md')
        self.assertIn('Never modify company data, style', updates)
        self.assertIn('Do not rebuild the same', updates)
        self.assertIn('version with different content', updates)

    def test_manifest_complete_and_verified(self):
        release=guard.load_manifest(ROOT)
        self.assertEqual(release['version'], '1.5.1')
        managed=set()
        for path in ROOT.rglob('*'):
            if not path.is_file():
                continue
            rel=path.relative_to(ROOT).as_posix()
            if rel == 'release.json':
                continue
            if guard.managed(rel):
                managed.add(rel)
        self.assertEqual(set(release['files']), managed)
        for required in ('references/signature.md','references/updates.md','references/master-brain.md','assets/update-task.json','scripts/update_guard.py'):
            self.assertIn(required, release['files'])

    def test_no_private_profiles_in_package(self):
        for rel in ('profil','profiles','backups'):
            self.assertFalse((ROOT/rel).exists())
        private={'user-style.md','company-profile.txt','user-style.txt','profile-history.md'}
        for path in ROOT.rglob('*'):
            if path.is_file() and path.name in private:
                self.fail(f'Private profile file bundled: {path}')

    def test_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' not in target and not target.startswith(('#','mailto:')):
                    self.assertTrue((path.parent/target.split('#')[0]).is_file(), (str(path), target))

    def test_utf8_and_no_private_recordings(self):
        for path in ROOT.rglob('*'):
            if path.is_file() and path.suffix in ('.md','.txt','.json','.yaml','.yml'):
                value=path.read_text(encoding='utf-8')
                self.assertNotIn('\ufffd', value, str(path))
                self.assertNotIn('fathom.video/share/', value, str(path))


if __name__ == '__main__':
    unittest.main(verbosity=2)
