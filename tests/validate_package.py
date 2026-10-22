#!/usr/bin/env python3
"""Static package checks, not a ChatGPT Desktop integration test."""
import hashlib
import json
import re
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
BASELINES = json.loads((ROOT/'tests/expected-hashes.json').read_text())

class PackageChecks(unittest.TestCase):
    def test_entrypoints(self):
        for name in ('START.md','SKILL.md','AGENTS.md','INSTRUKCJA-KLIENTA.md','VERSION'):
            self.assertTrue((ROOT/name).is_file(),name)
        self.assertEqual((ROOT/'VERSION').read_text().strip(),'1.2.0')
    def test_one_skill(self):
        self.assertEqual([p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md')],['SKILL.md'])
    def test_sample_unchanged(self):
        self.assertEqual(hashlib.sha256((ROOT/'references/master-sample.md').read_bytes()).hexdigest(),BASELINES['master_sample'])
    def test_core_unchanged(self):
        self.assertEqual(hashlib.sha256((ROOT/'references/master-brain.md').read_bytes()).hexdigest(),BASELINES['master_brain'])
    def test_links(self):
        docs=[ROOT/'README.md',ROOT/'SKILL.md',*[p for p in (ROOT/'references').glob('*.md') if p.name!='project-setup.md']]
        for p in docs:
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
                if '://' not in target and not target.startswith(('#','mailto:')):
                    self.assertTrue((p.parent/target.split('#')[0]).is_file(),(p.name,target))
    def test_no_private_profiles(self):
        private={'company-profile.md','user-style.md','company-profile.txt','user-style.txt','profile-history.md'}
        for p in ROOT.rglob('*'):
            if p.is_file() and p.parent.name!='references':
                self.assertNotIn(p.name,private)
    def test_templates(self):
        for p in (ROOT/'assets').glob('*.template.txt'):
            t=p.read_text(encoding='utf-8')
            for s in ('approval: TEMPLATE','revision: 0','tool_version: 1.2.0'):
                self.assertIn(s,t)
    def test_ignore(self):
        t=(ROOT/'.gitignore').read_text()
        for s in ('/profil/','**/user-style.md','!/references/company-profile.md','.env'):
            self.assertIn(s,t)
    def test_utf8(self):
        for p in ROOT.rglob('*'):
            if p.is_file() and p.suffix in ('.md','.txt','.yaml'):
                t=p.read_text(encoding='utf-8')
                self.assertNotIn('\ufffd',t,p.name)
                self.assertNotIn('fathom.video/share/',t,p.name)
                self.assertIsNone(re.search(r'~[acelnoszxACELNOSZX]',t),p.name)
    def test_persistence(self):
        t=(ROOT/'references/local-workspace.md').read_text(encoding='utf-8')
        for s in ('ROOT/profil/company-profile.md','ROOT/profil/user-style.md','revision','company_key','backups'):
            self.assertIn(s,t)
    def test_metadata(self):
        t=(ROOT/'agents/openai.yaml').read_text(encoding='utf-8')
        self.assertIn('display_name:',t)
        self.assertIn('short_description:',t)

if __name__=='__main__':
    unittest.main(verbosity=2)
