# Testing and Deployment Results

## Tests and checks

Run the unit suite with explicit paths:

```powershell
python -m pytest tests\test_submission.py tests\test_reviewer.py -v
```

Run Selenium only after a reachable app is deployed:

```powershell
$env:APP_BASE_URL = "http://127.0.0.1:5001"
python -m pytest tests\selenium -v
```

**Executed results:**

- Unit tests: `python -m pytest tests\test_submission.py tests\test_reviewer.py -v` — 15 passed.
- PowerShell parser: all four Week 12 PowerShell scripts parsed successfully.
- Docker image: `docker build -t news-publishing-app:week12 -t news-publishing-app:week12-build-local .` — succeeded.
- Deployment: `scripts\deploy_docker.ps1` created `news-publishing-container` using `news-publishing-data`; a second run replaced the container successfully.
- Health: `scripts\verify_container.ps1` reported running and healthy; Docker inspect reported `healthy`; `python scripts\healthcheck.py 127.0.0.1 5001 1` returned HTTP 200 with the expected response.
- Port and logs: Docker reported host port 5001 mapped to container port 5001 on IPv4 and IPv6; Gunicorn startup and `/health` access appeared in container logs.
- SQLite: article ID 9 was created before a deployment replacement and was still retrievable afterward with status `SUBMITTED`.
- Selenium: after correcting the existing page-load assertion to match the actual `Submit News Article` page title, `APP_BASE_URL=http://127.0.0.1:5001 python -m pytest tests\selenium -v` — 8 passed.

The initial candidate check briefly failed because a temporary filesystem mount hid the app user's writable `/data`; the candidate now uses its disposable container filesystem, and both subsequent deployments succeeded. The old Selenium page-title assertion also failed once before being corrected; application UI was not changed.

**Not verified:** Jenkins itself was not run. Although Docker works in the interactive account, the Jenkins Windows service runs as `LocalSystem`, and access to the Docker Desktop engine under that service identity remains unverified. Configure and test that prerequisite on the Jenkins host before claiming a Jenkins build succeeded. Existing unrelated containers and images were not modified. No screenshots were captured.
