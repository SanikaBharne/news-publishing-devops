# NewsFlow reader and publisher experience

## What changed

The existing Flask/Jinja/SQLite application now has a NewsFlow editorial design across its public edition, reader sign-in/reading list, publisher workspace/editor, article preview, and reviewer queue. The Reviewer Desk also shows the latest recorded project test results and milestones, clearly distinguished from live Jenkins telemetry. Vanilla JavaScript loads the approved public feed, supports title/author/story search, category and date sorting, and submits publisher articles through the existing JSON API. Readers can open approved articles and save them to a persistent reading list. Publishers can save drafts, preview, submit, review another publisher's submissions, and see rejection notes.

The backend keeps the existing article API paths and status values. `SUBMITTED` remains the review-queue status; public pages expose only `APPROVED` articles. Draft/rejected edits use publisher pages; the reviewer table and approve/reject APIs remain. The existing `/health` contract and default port 5001 remain unchanged. The Jenkins unit stage now includes the new authorization/public-access tests.

## Access and persistence

Reader and Publisher are the only account roles. Editorial review uses a second Publisher account; a publisher cannot approve or reject their own account-owned submission. Passwords are hashed, role checks happen server-side, and mutations require a session CSRF token. There is no open registration, `PUBLISHED` status, localStorage workflow, or article deletion.

Startup creates `users` and `bookmarks`, and adds `summary`, `category`, `cover_image`, and nullable `user_id` columns to an existing `articles` table using additive migrations. Existing article rows/statuses remain. Session signing uses `SECRET_KEY` if configured or a generated private key file alongside the configured SQLite database. For Docker the key file remains under `/data` with the existing database volume. Keep the DB, key file, and `news-publishing-data` volume together.

See [account setup](newsflow-accounts.md) for interactive local and Docker account creation; no demo credentials are committed. When a role has no provisioned account, its login screen now explains how to create one interactively without putting a password in shell history.

## Verification record

- `python -m pytest tests\test_submission.py tests\test_reviewer.py tests\test_auth_public.py -v` — **24 passed**, including the end-to-end approval-to-public-feed regression test.
- `python -m pytest tests\selenium -v` — **9 passed**, including the reader browse/bookmark flow, publisher submission, separate reviewer approval/rejection, and validation.
- `docker build -t news-publishing-app:newsflow-redesign .` — **passed**. The rebuilt image was deployed to `news-publishing-container` on 2026-10-13 after saving a database-volume backup; `news-publishing-data` remained mounted and was not removed.
- Live deployment verification — **passed**. The new container reported `healthy`, `/health` returned HTTP 200 with `status: ok`, and the Publisher login page displayed the missing-account setup instructions.
- The persistent `users` table was empty at deployment time, so Reader/Publisher sign-in cannot succeed until accounts are provisioned using the interactive commands in [account setup](newsflow-accounts.md). The form/authentication flow itself is covered by local tests.
- The PyCharm build command returned success but reported that this project has limited build-diagnostics support.
- Jenkins was not run or independently checked. The existing Jenkins read endpoint requires authentication; no Jenkins credentials were supplied.

## Safe deployment boundary

Automated tests use an ephemeral local Flask server and a temporary SQLite database. The production update reused the existing `news-publishing-data` volume; a volume backup was saved under the Windows temp directory and the previous container was retained as `news-publishing-redesign-backup` for rollback. Jenkins was not used for this deployment. Never remove the named data volume.
