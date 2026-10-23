# QA report - Wedding Mail Assistant 1.4.0

Verification performed 2026-10-23 in an isolated build container.

- Baseline unpacked from the supplied v1.3.0 ZIP; the full Git tree was identical to
  repository tree b72401eddf958624546231ef7326f4c7806245a6 (commit 3330457).
- 25 existing package and business-workflow checks passed.
- 17 new updater checks passed: consent binding, local edits/backup, rollback after a
  handled write error, stable version ordering, tampering, private/unsafe paths,
  symlinks, concurrency lock, preserved unknown files and protected client data.
- Master Brain, Master Sample v3.0, the 16 questions and the demo fixture remain
  byte-for-byte equal to their approved hashes.
- Stable release manifest validates hashes of all managed publisher files.
- Skill structure validation and ZIP integrity checked before delivery.

## Limits of verification
No real customer desktop was accessed. No customer profiles were read, migrated or written.
These are deterministic file/helper tests, not an end-to-end model test or proof that a
customer's native scheduler was activated. Activation must use the scheduler API and read
its actual returned status in that customer's environment. A cloud watch cannot inspect a
local installation. Handled failures roll back; abrupt power/process loss can need recovery.
Hash manifests verify file consistency, not publisher signatures. No remote hooks execute.
