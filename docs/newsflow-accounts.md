# NewsFlow accounts and local setup

NewsFlow has two sign-in roles: **Reader** and **Publisher**. There is no public account registration. Passwords are stored as Werkzeug password hashes, and pages/actions check roles on the server.

## Existing Flask / Windows setup

From the project root in Windows PowerShell, set account values for the current process only, then run the existing deploy script. Choose private values locally; do not commit credentials or use real production passwords in academic screenshots.

```powershell
$env:SECRET_KEY = [guid]::NewGuid().ToString('N') + [guid]::NewGuid().ToString('N')
$env:DEMO_READER_USERNAME = 'reader-demo'
$securePassword = Read-Host 'Choose a reader demo password' -AsSecureString
$env:DEMO_READER_PASSWORD = [System.Net.NetworkCredential]::new('', $securePassword).Password
$env:DEMO_PUBLISHER_USERNAME = 'publisher-demo'
$securePassword = Read-Host 'Choose a publisher demo password' -AsSecureString
$env:DEMO_PUBLISHER_PASSWORD = [System.Net.NetworkCredential]::new('', $securePassword).Password
$env:DEMO_REVIEWER_USERNAME = 'reviewer-demo'
$securePassword = Read-Host 'Choose a separate publisher/reviewer demo password' -AsSecureString
$env:DEMO_REVIEWER_PASSWORD = [System.Net.NetworkCredential]::new('', $securePassword).Password
python scripts\deploy.py
```

`init_db()` seeds or updates only the named demo accounts when both username and password environment variables are supplied. It creates the new account/bookmark tables and adds optional article columns with `ALTER TABLE`; it does not delete or recreate existing article data. Without `SECRET_KEY`, the app creates a random key beside the configured SQLite file and reuses it across worker processes/restarts. Keep this `.secret` file private and preserve it with the database.

The deploy script uses port 5001 by default. `APP_PORT` can override it for isolated development/test runs.

## Docker account setup

After the image/container has initialized its existing SQLite volume, create accounts interactively; no password is included in a command or source file:

```powershell
docker exec -it news-publishing-container python -m src.manage_users --role reader --username reader-demo --name "Reader Demo"
docker exec -it news-publishing-container python -m src.manage_users --role publisher --username publisher-demo --name "Publisher Demo"
docker exec -it news-publishing-container python -m src.manage_users --role publisher --username reviewer-demo --name "Reviewer Demo"
```

Each command prompts for and confirms a 12-character-minimum password. These commands alter only the account table in the existing named volume; they do not remove the container or database. Do not put passwords in PowerShell command history.

## Workflow and access

- The public homepage and `/api/public/articles` expose **APPROVED** articles only. `/article/<id>` and `/api/public/articles/<id>` return 404 for drafts, submissions, and rejected articles.
- Readers can save only approved stories to their reading list.
- Publishers create drafts or submit stories (`SUBMITTED`), then a different publisher account can approve (`APPROVED`) or reject (`REJECTED`) them. Rejection requires a non-whitespace comment; a publisher cannot review their own account-owned submission.
- Existing article APIs remain under `/api/articles` and are publisher-only. State-changing forms/API requests require a session CSRF token.
- Approval is the public MVP boundary; there is no `PUBLISHED` state.

For production HTTPS, provide a stable high-entropy `SECRET_KEY` via the service's secret environment configuration and set `SESSION_COOKIE_SECURE=true`. Keep demo account credentials in a local secret manager/environment, never in Git.
