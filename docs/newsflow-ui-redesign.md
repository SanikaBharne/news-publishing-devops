# NewsFlow reader and publisher experience

## What changed

The existing Flask/Jinja/SQLite application now has a NewsFlow editorial design across its public edition, reader sign-in/reading list, publisher workspace/editor, article preview, and reviewer queue. Vanilla JavaScript loads the approved public feed, supports title/author/story search, category and date sorting, and submits publisher articles through the existing JSON API. Readers can open approved articles and save them to a persistent reading list. Publishers can save drafts, preview, submit, review another publisher's submissions, and see rejection notes.

The backend keeps the existing article API paths and status values. `SUBMITTED` remains the review-queue status; public pages expose only `APPROVED` articles. Draft/rejected edits use publisher pages; the reviewer table and approve/reject APIs remain. The existing `/health` contract and default port 5001 remain unchanged. The Jenkins unit stage now includes the new authorization/public-access tests.

## Access and persistence

Reader and Publisher are the only account roles. Editorial review uses a second Publisher account; a publisher cannot approve or reject their own account-owned submission. Passwords are hashed, role checks happen server-side, and mutations require a session CSRF token. There is no open registration, `PUBLISHED` status, localStorage workflow, or article deletion.

Startup creates `users` and `bookmarks`, and adds `summary`, `category`, `cover_image`, and nullable `user_id` columns to an existing `articles` table using additive migrations. Existing article rows/statuses remain. Session signing uses `SECRET_KEY` if configured or a generated private key file alongside the configured SQLite database. For Docker the key file remains under `/data` with the existing database volume. Keep the DB, key file, and `news-publishing-data` volume together.

See [account setup](newsflow-accounts.md) for interactive local and Docker account creation; no demo credentials are committed.

## Verification record

- `python -m pytest tests\test_submission.py tests\test_reviewer.py tests\test_auth_public.py -v` — **21 passed**.
- `python -m pytest tests\selenium -v` — **9 passed**, including the reader browse/bookmark flow, publisher submission, separate reviewer approval/rejection, and validation.
- `python scripts\healthcheck.py 127.0.0.1 5001 1` — **passed** against the currently running deployment. The same health script also passed against a temporary isolated Flask/SQLite instance. The existing deployment was not replaced.
- `docker build -t news-publishing-app:newsflow-redesign .` — **passed**. This built the source assets into a new local image tag; no live container was restarted or redeployed.
- The PyCharm build command returned success but reported that this project has limited build-diagnostics support.
- Jenkins was not run or independently checked. The existing Jenkins read endpoint requires authentication; no Jenkins credentials were supplied.

## Safe deployment boundary

The tests use an ephemeral local Flask server and a temporary SQLite database. The existing container at port 5001 and its `news-publishing-data` volume were not changed. The newly built image has not been deployed or runtime-smoke-tested as a container. Before replacing the live deployment, verify Jenkins in an authenticated session and use the existing candidate-health/rollback deployment workflow. Never remove the named data volume.
