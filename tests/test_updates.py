#!/usr/bin/env python3
"""Updater safety tests on temporary fictional installations, no user data/network."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import update_guard as guard


def write_release(root, ver):
    root.mkdir(parents=True, exist_ok=True)
    contents = {'VERSION': ver + '\n', 'SKILL.md': '# Tool ' + ver,
                'START.md': '# Start ' + ver, 'references/master-sample.md': '# Sample ' + ver}
    for name, value in contents.items():
        p=root/name; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(value, encoding='utf-8')
    release = {'schema_version': 1, 'repository': guard.REPO, 'channel': 'stable',
               'version': ver, 'files': {n:guard.digest((root/n).read_bytes()) for n in contents}}
    (root/'release.json').write_text(json.dumps(release), encoding='utf-8')
    return release


class UpdateChecks(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.tool=self.root/'narzedzie'; self.stage=self.root/'stage'
        write_release(self.tool,'1.4.0'); write_release(self.stage,'1.5.0')

    def do_apply(self, **kw):
        p=guard.plan(self.tool,self.stage)
        return guard.apply(self.tool,self.stage,p['plan_id'],p['to_version'],**kw)

    def test_numeric_versions(self):
        self.assertGreater(guard.version('1.10.0'),guard.version('1.9.0'))
        for v in ['1.4','v1.4.0','1.4.0-beta','01.4.0','../2.0.0']:
            with self.assertRaises(ValueError): guard.version(v)

    def test_plan_is_read_only(self):
        before={p.relative_to(self.tool):p.read_bytes() for p in self.tool.rglob('*') if p.is_file()}
        p=guard.plan(self.tool,self.stage)
        self.assertEqual(p['local_changes'],[])
        after={p.relative_to(self.tool):p.read_bytes() for p in self.tool.rglob('*') if p.is_file()}
        self.assertEqual(before,after)

    def test_apply_requires_version_and_plan_consent(self):
        p=guard.plan(self.tool,self.stage)
        for plan, ver in [('',p['to_version']),(p['plan_id'],''),(p['plan_id'],'1.6.0')]:
            with self.assertRaises(ValueError): guard.apply(self.tool,self.stage,plan,ver)
        self.assertEqual((self.tool/'VERSION').read_text().strip(),'1.4.0')

    def test_update_keeps_customer_files_inside_and_outside(self):
        private=[self.root/'profil/company-profile.md',self.root/'profil/user-style.md',
                 self.tool/'profil/company-profile.md',self.tool/'notes.txt',self.root/'START.md']
        for p in private:
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b'CLIENT DATA\x00unchanged')
        result=self.do_apply()
        self.assertTrue(result['updated'])
        for p in private: self.assertEqual(p.read_bytes(),b'CLIENT DATA\x00unchanged')
        self.assertEqual(guard.load_manifest(self.tool)['version'],'1.5.0')
        self.assertTrue((Path(result['backup'])/'SKILL.md').is_file())

    def test_manual_master_requires_warning_consent_and_is_backed_up(self):
        p=self.tool/'references/master-sample.md';p.write_text('MY MASTER',encoding='utf-8')
        proposed=guard.plan(self.tool,self.stage)
        self.assertIn('references/master-sample.md', proposed['local_changes'])
        with self.assertRaises(ValueError): self.do_apply()
        self.assertEqual(p.read_text(),'MY MASTER')
        result=self.do_apply(overwrite_local=True)
        self.assertEqual((Path(result['backup'])/'references/master-sample.md').read_text(),'MY MASTER')

    def test_no_manifest_means_conservative_legacy_warning(self):
        (self.tool/'release.json').unlink()
        self.assertTrue(guard.plan(self.tool,self.stage)['local_changes'])
        with self.assertRaises(ValueError): self.do_apply()

    def test_stale_plan_rejected_after_local_change(self):
        p=guard.plan(self.tool,self.stage)
        (self.tool/'SKILL.md').write_text('Changed after yes',encoding='utf-8')
        with self.assertRaises(ValueError):
            guard.apply(self.tool,self.stage,p['plan_id'],p['to_version'],True)

    def test_staged_content_tamper_rejected(self):
        (self.stage/'SKILL.md').write_text('Tampered',encoding='utf-8')
        with self.assertRaises(ValueError): self.do_apply()

    def test_unsafe_manifest_entries(self):
        base=json.loads((self.stage/'release.json').read_text())
        for name in ['../profil/user-style.md','/tmp/x','C:/x','references/../../x',
                     'profil/company-profile.md','assets/user-style.md','references/.env',
                     'scripts/backups/x.py','.git/config','scripts\\x.py']:
            m=copy.deepcopy(base);m['files'][name]='0'*64
            (self.stage/'release.json').write_text(json.dumps(m),encoding='utf-8')
            with self.subTest(name=name),self.assertRaises(ValueError):
                guard.load_manifest(self.stage,verify=False)

    def test_wrong_repo_or_channel_rejected(self):
        base=json.loads((self.stage/'release.json').read_text())
        for key,value in [('repository','attacker/repo'),('channel','beta')]:
            m=copy.deepcopy(base);m[key]=value
            (self.stage/'release.json').write_text(json.dumps(m),encoding='utf-8')
            with self.assertRaises(ValueError):guard.load_manifest(self.stage)

    def test_symlink_target_blocked(self):
        target=self.tool/'references/master-sample.md'; target.unlink()
        victim=self.root/'victim'; victim.write_text('PRIVATE')
        try:target.symlink_to(victim)
        except OSError:self.skipTest('Symlinks unavailable')
        with self.assertRaises(ValueError):self.do_apply(overwrite_local=True)
        self.assertEqual(victim.read_text(),'PRIVATE')

    def test_downgrade_and_same_version_blocked(self):
        for ver in ['1.4.0','1.3.9']:
            write_release(self.stage,ver)
            with self.assertRaises(ValueError):guard.plan(self.tool,self.stage)

    def test_version_manifest_mismatch(self):
        m=json.loads((self.stage/'release.json').read_text());m['version']='1.6.0'
        (self.stage/'release.json').write_text(json.dumps(m),encoding='utf-8')
        with self.assertRaises(ValueError):guard.plan(self.tool,self.stage)

    def test_concurrent_lock_preserved(self):
        lock=self.tool/'.wma-updates/apply.lock';lock.parent.mkdir();lock.write_text('other')
        with self.assertRaises(FileExistsError):self.do_apply()
        self.assertEqual(lock.read_text(),'other')

    def test_handled_write_failure_rolls_back(self):
        original={name:(self.tool/name).read_bytes() for name in guard.load_manifest(self.tool)['files']}
        original['release.json']=(self.tool/'release.json').read_bytes()
        real=guard.atomic_write; failed=[False]
        def fail_once(p,data):
            if p==self.tool/'START.md' and not failed[0]:
                failed[0]=True;raise OSError('Simulated disk error')
            return real(p,data)
        with patch.object(guard,'atomic_write',side_effect=fail_once):
            with self.assertRaises(OSError):self.do_apply()
        for name,data in original.items():self.assertEqual((self.tool/name).read_bytes(),data)
        self.assertFalse((self.tool/'.wma-updates/apply.lock').exists())

    def test_missing_required_file_rejected(self):
        m=json.loads((self.stage/'release.json').read_text());del m['files']['START.md']
        (self.stage/'release.json').write_text(json.dumps(m),encoding='utf-8')
        with self.assertRaises(ValueError):guard.load_manifest(self.stage)

    def test_scheduler_policy_and_stable_manifest(self):
        task=json.loads((ROOT/'assets/update-task.json').read_text())
        self.assertEqual(task['timing_mode'],'condition_watch')
        self.assertIn('FREQ=DAILY;BYHOUR=8',task['schedule'])
        self.assertFalse(task['auto_install'])
        self.assertTrue(task['require_user_consent_for_each_update'])
        self.assertEqual(guard.load_manifest(ROOT)['version'],'1.4.0')


if __name__=='__main__':
    unittest.main(verbosity=2)
