# Week 15 - Final Testing Report

**Execution date:** 2026-10-31
**Python:** 3.14.7
**Test runner:** pytest 9.1.1

## Python unit/backend tests

Command:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_submission.py tests\test_reviewer.py tests\test_auth_public.py -v
```

| Collected | Passed | Failed | Skipped | pytest-reported duration | Command wall time |
|---:|---:|---:|---:|---:|---:|
| 24 | 24 | 0 | 0 | 15.25 s | 16.45 s |

The suite covered submission validation and persistence, dashboard listing, approval/rejection and status APIs, authentication and role restrictions, CSRF, public article access, bookmarks, and publisher/reviewer restrictions. The cross-role regression test that approves a submitted article and then reads it from the Reader edition passed.

## Selenium UI automation

Command:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\selenium -v
```

| Collected | Passed | Failed | Skipped | pytest-reported duration | Command wall time |
|---:|---:|---:|---:|---:|---:|
| 9 | 9 | 0 | 0 | 62.44 s | 63.73 s |

The suite started its own isolated Flask server, used a temporary SQLite database and test-only accounts, and exercised headless Chrome. Submission, reviewer dashboard, approval, rejection with a comment, Reader browsing/bookmarking, empty-form validation, and whitespace validation all passed. It did not use or change the project's `app.db`.

## Integration tests

There is no distinct integration-test directory or separately configured integration runner. Integration behavior is covered by the backend cross-role regression test and by the Selenium end-to-end suite; their results are included above and must not be added again to the total.

## Jenkins pipeline

The Jenkinsfile defines these stages: **Checkout**, **Check Python**, **Install Dependencies**, **Run Unit Tests**, **Build Docker Image**, **Deploy Docker Container**, **Health Check**, **Run Selenium Tests**, and **Final Verification**.

| Stage | Week 15 actual result |
|---|---|
| Checkout | Not run - Jenkins unavailable |
| Check Python | Not run - Jenkins unavailable |
| Install Dependencies | Not run - Jenkins unavailable |
| Run Unit Tests | Not run in Jenkins; local suite passed 24/24 |
| Build Docker Image | Not run - Docker Engine unavailable |
| Deploy Docker Container | Not run - Jenkins/Docker unavailable |
| Health Check | Not run against a deployment |
| Run Selenium Tests | Not run in Jenkins; local suite passed 9/9 |
| Final Verification | Not run - Jenkins unavailable |

The check of `http://127.0.0.1:8080/login` timed out without a response. No Jenkins build was triggered, so there is no actual Week 15 build number, stage result, or console output. Historical pipeline results are not evidence of a current run.

## Docker and application health

- `docker.exe` is installed, but Docker commands could not connect to `npipe:////./pipe/dockerDesktopLinuxEngine`; the Linux engine was not running/available.
- No image build, container start/restart, log inspection, volume inspection, or deployment was performed.
- The application endpoint at `http://127.0.0.1:5001/health` was unreachable during the check.
- The Selenium fixture did start an isolated application and required a successful HTTP 200 response from `/health` before running the browser tests. This verifies the test server, not the deployed container.
- The root `app.db` was opened read-only. SQLite reported `integrity_check=ok` and 33 article rows. No claim is made about a Docker volume or persistence across a container restart in Week 15.

## Result and limitations

**Local application tests: PASS (33/33 total across the two separately run suites).** There were no test failures or skips. Jenkins, Docker build/deployment, live application health, and deployed-volume persistence remain **unverified** because the required services were unavailable. No tests were modified to obtain these results.
