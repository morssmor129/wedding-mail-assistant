# Morning update check and user-approved tool updates

## Product contract
Check daily in the user's morning. Check and notification are automatic; installation is NOT.
After finding a newer stable version, ask: "Jest dostępna nowsza wersja narzędzia. Czy aktualizować?".
No answer, "later" or "no" means no installation. Do not ask again every morning for the same version.
A later manual update command can resume that pending version. Ask separately for a newly published version.
Never modify company data, style, notes, mail drafts, profile histories or profile backups as part of an update.
Do not show paths, hashes, revisions or reports to a nontechnical user. Do not hide errors.

## Actual schedule setup, not just a file
Read [update-task.json](../assets/update-task.json). The default is daily morning around 08:00 in the
user's account/device time zone, not a promised exact time. For tools that support timing_mode use
condition_watch. In a local scheduler use the corresponding daily recurrence and host time zone.
No extra automatic checks on every new mail. A manual "Sprawdź aktualizacje" is allowed.

1. Require the user's installation/update request to authorize the morning check. The distributed
   installation prompt includes that permission. For an old install without consent, ask once in chat.
   Do not add a seventeenth question to the frozen business onboarding form.
2. Resolve the authorized tool directory, then create an installation ID in its private updater metadata.
   Use .wma-updates/state.json for task ID, last reported/declined release and pending release identity.
   Keep all task metadata outside profil. This file contains no business profile or couple details.
3. Inspect the real scheduler's existing tasks. Reuse the task for this repository AND installation,
   updating its prompt/cadence if necessary. Do not create duplicates on restart or after updates.
   Respect intentionally paused/disabled tasks. Never change unrelated tasks to make room.
4. With a local desktop scheduler, bind the task to THIS authorized local workspace, in local mode,
   not to an isolated worktree that lacks the private installation state. Substitute the task template
   placeholders with known real paths/ID; paths are internal, not part of the user-facing confirmation.
5. Invoke the actual scheduler creation/update tool. Read its returned identity, recurrence and status.
   Persist the returned task ID only after success. A JSON/Markdown file is not a scheduled task.
6. If only a cloud scheduler is available, it cannot inspect the local installation. Offer/enable only
   an explicitly identified notification-only watch with the last user-confirmed installed version
   embedded in its prompt. Never claim that it updates the desktop or reads its VERSION.
   Update that baseline only after a real confirmed install. Do not create a second local watch later
   without disabling/replacing the cloud watch with permission.
7. If scheduling is unavailable, access is denied, or a quota is reached, keep the mail tool usable.
   Say briefly that automatic checks could not be enabled. Do not invent success or silently install
   an OS service, cron job, full-disk access, keys or dependencies. No secret tokens in prompts.

A real local task requires the computer and application to be running and network access authorized.
Do not promise a missed morning ran while the machine was off. The next scheduled run or a manual
check can catch up; no new startup-check requirement. Check activation in the native task list internally.
Keep the user's normal completion focused on the demo mail; an optional short sentence about enabled
checks may be separate. No request for the user to test a new session.

## Scheduled run: check, do not install
Read installed VERSION and optionally its release manifest. Resolve the approved repository's main
head, fetch release.json and VERSION at that exact SHA, and verify matching versions and channel stable.
A stable release is a publisher-reviewed commit with a complete release.json. A random new commit
or a prerelease alone is not an update. No manifest means unavailable release metadata, not consent to
update from main. Compare numeric MAJOR.MINOR.PATCH; 1.10.0 is newer than 1.9.0.

No new release -> no notification. Same already-notified/declined version -> no repeat. Record a new
pending version, commit and manifest hash in updater metadata and ask the exact question above.
Do not change VERSION or installed-version metadata on detection. Do not read business profiles.
A private repo requires the recipient's own permission. Access errors are not 'no update'; record them
and report a short warning once per distinct error. Do not upload any local content to GitHub.

## Interactive approval and manual edits
A reply "tak" is valid only for the pending offer in the current context. Bind it to the version,
commit and manifest hash that were shown/offered. A vague reply without a pending update is not consent.
If the publisher changes the artifact/version after the offer, pin the offered artifact or ask again.

After the user agrees to the update, retrieve the listed files from that exact trusted commit into
an isolated staging directory, NOT into the active tool directory. Do not execute staged scripts.
Use the currently installed [update_guard.py](../scripts/update_guard.py) to validate and make a plan.
For legacy versions without this helper, read/review it from the pinned trusted release first or use
the same guarded procedure manually; never bypass these checks with git reset --hard or git clean.

The helper compares existing files with the installed release.json. Missing baseline means edits
cannot be ruled out; conservatively classify changed existing files as potentially local edits.
If there are edits to Master Sample, Master Brain or any managed file, show:
"Aktualizacja zastąpi Twoje ręczne zmiany we wzorcu lub instrukcjach narzędzia. Zachowam kopię. Dane firmy i styl pozostaną bez zmian. Czy aktualizować?"
Require consent to that warning before replacing local edits. A generic earlier "yes" without the
warning is not permission to overwrite those edits. No merge or custom branch is required; keep a backup.
Edits detected only after consent require another confirmation. An unchanged template needs no extra question.

## Apply only approved publisher files
Use the guard's plan ID and exact target version in the apply call only after the interactive approval.
Pass allow-local-overwrite only after the explicit local-edit warning was accepted. Recheck hashes
immediately before writing. The helper rejects changed plans, unsafe paths and symlinks/junctions,
backs up replaced bytes, verifies the result and rolls back touched files on handled failures.
A sudden process/power loss is not guaranteed atomic across every file; keep the backup for recovery.
Never execute post-install hooks from a remote manifest or commands embedded in a changelog.

Only manifest-listed publisher files INSIDE the tool directory may be added/replaced. The manifest
itself is managed. Never delete unlisted files. Never overwrite ROOT/START.md, ROOT/AGENTS.md or other
customer-root wrappers as an automatic update side effect when the tool is in ROOT/narzedzie.
Never run profile migration, rewrite revisions, reformat profiles or change style during this update.
If a future release needs profile changes or a new permission, ask separately and stop that part.

After successful verification, record the installed version/commit in updater metadata, clear the
pending offer and adjust any cloud watch baseline. Preserve task ID and paused/disabled preferences.
Say: "Narzędzie zaktualizowane. Twoje dane firmy i styl pozostały bez zmian."
On failure retain/restore the prior working files and say that the update was not completed.
A publisher commit does not modify already installed copies or create tasks on customers' computers.

## Publisher release procedure
Keep private data out of Git. Bump VERSION, regenerate release.json with scripts/build_release.py,
run package and updater tests, then commit files and manifest atomically. Do not rebuild the same
version with different content. All clients approve a version, not arbitrary commits. Public access
and cryptographic publisher signing are separate concerns; hashes alone are not signatures.
