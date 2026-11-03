# NewsFlow - Final Deployment Guide

This guide documents the existing Flask/SQLite application and Windows Jenkins-to-Docker pipeline. It does not imply that Jenkins or Docker was available during the Week 15 validation.

## Prerequisites

- Windows PowerShell for the existing deployment scripts and Jenkins pipeline (`bat` and `powershell.exe` steps).
- Python and pip. The Week 15 host test environment used Python 3.14.7; the Dockerfile uses Python 3.12.
- Google Chrome for Selenium UI tests. Selenium runs headless Chrome and starts its own isolated local test server.
- Docker Desktop with the **Linux** engine available to the invoking user/service account for image/container operations.
- A configured Jenkins controller and Windows agent with Git, Python, Docker CLI/engine access, Chrome, and required Python packages.

## Local environment setup

From the repository root, create a virtual environment only if one is not already available:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The Week 15 suites were run with the project's existing `.venv`. The default database path is `app.db`. Preserve that file and its adjacent `.secret` file; do not delete, replace, or initialize against it unless that is the intended data set. For an isolated new local instance, set `DATABASE_PATH` to a new file path before starting the application. Do not set `DEMO_*_PASSWORD` values in source or commit them.

To start the Windows-compatible local server:

```powershell
.\.venv\Scripts\python.exe scripts\deploy.py
```

The server listens on `127.0.0.1:5001` by default. `APP_PORT` can select another port. Startup calls `init_db()`, which applies additive schema changes and seeds demo accounts only when the corresponding username and password environment-variable pairs are supplied. Do not run against existing data without understanding the configured database path.

Local URLs:

- Application: `http://127.0.0.1:5001/`
- Health: `http://127.0.0.1:5001/health`

For role demonstrations, use `python -m src.manage_users --role reader --username <name> --name "<display name>"` and repeat with `--role publisher`. The command prompts for a confirmed password of at least 12 characters. A second Publisher account is used for editorial review; there is no separate reviewer role. Never place passwords in a command, source file, screenshot, or Git.

## Automated tests

Run the backend and Selenium suites separately from the project root:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_submission.py tests\test_reviewer.py tests\test_auth_public.py -v
.\.venv\Scripts\python.exe -m pytest tests\selenium -v
```

The Selenium fixture starts a temporary server and uses a temporary SQLite database; do not start a second application for that suite. The current verified results are in the [testing report](final-testing-report.md).

## Docker image and deployment

First confirm Docker Engine availability and build the image:

```powershell
docker info
docker build -t news-publishing-app:week15 .
```

The image exposes port 5001, runs Gunicorn as a non-root user, and sets `DATABASE_PATH=/data/app.db`. The existing deployment configuration uses the named volume `news-publishing-data` mounted at `/data`.

The existing deployment helper performs a **deployment**, not a read-only check. It may stop and replace the named application container; after a successful replacement it removes the renamed previous container. It preserves the configured named database volume, but do not run it against existing project data without authorization and a verified backup:

```powershell
.\scripts\deploy_docker.ps1 `
  -Image "news-publishing-app:week15" `
  -ContainerName "news-publishing-container" `
  -VolumeName "news-publishing-data" `
  -HostPort 5001 `
  -BuildId "week15-manual"
```

Never run `docker volume rm` or remove/recreate the database volume as part of validation. After an authorized deployment, verify:

```powershell
docker ps --filter "name=^news-publishing-container$"
docker inspect --format "State={{.State.Status}} Health={{.State.Health.Status}}" news-publishing-container
docker inspect --format "{{range .Mounts}}{{.Name}}:{{.Destination}} {{end}}" news-publishing-container
docker logs --tail 50 news-publishing-container
.\.venv\Scripts\python.exe scripts\healthcheck.py 127.0.0.1 5001 3
```

Expected: running/healthy, the expected volume mounted at `/data`, no critical runtime errors in the log tail, and an HTTP 200 `/health` response with `"status":"ok"`. Check article persistence across a planned replacement only in an authorized deployment window, and verify against a known non-sensitive test record. Jenkins build #4 later built and deployed the current image to isolated staging successfully; persistence after restarting that exact deployed container remains unverified.

## Jenkins execution

The root `Jenkinsfile` is Windows-agent-specific. Configure the Jenkins Pipeline job SCM to use the intended repository and branch, confirm that the service account can run Python and access the Docker Linux engine, and configure the Jenkins Maven installation named `Maven-3.9.16`. The root `pom.xml` uses Maven's `validate` phase to run Python `compileall` on `src` and `scripts`; Maven validates Python syntax and does not compile the Flask application.

Stages, in order, are Checkout, Check Python, Install Dependencies, Maven Validation, Run Unit Tests, Build Docker Image, Deploy Docker Container, Health Check, Run Selenium Tests, and Final Verification. Selenium uses its isolated temporary application; the separate health-check stages verify the deployed staging URL.

The Week 15 pipeline uses the isolated staging container `newsflow-week15-staging`, volume `newsflow-week15-staging-data`, and host port `5016`; it must not be changed to reuse the existing application container or database volume for validation. The historical Week 12 job has a different SCM branch and deployment target, so confirm its configuration before triggering it.

Jenkins URL, when running locally: `http://127.0.0.1:8080/`. The Maven-enabled Week 15 job `NewsFlow-Week15-Final` passed build #4 on commit `928aebe`. Its console log is saved at `docs/evidence/week-15/jenkins-build-4-console.txt`.

## Troubleshooting

- **Docker named-pipe/engine error:** Start Docker Desktop's Linux engine, verify `docker info` succeeds for the Jenkins service identity, then retry. Do not remove containers or volumes to resolve an engine-availability error.
- **Port 5001 is occupied:** Identify the process/container owner first. Use a different `APP_PORT` for local development; do not terminate an unknown listener.
- **Health check fails:** Check the application/container state and recent logs, then verify the published host port and expected volume. Do not infer success from image build alone.
- **Login reports no account configured:** Create the relevant Reader or Publisher account using the interactive account-management command. Do not expose credentials in shell history.
- **Selenium cannot start Chrome:** Install/update Chrome and confirm Selenium can obtain a compatible driver; run the suite again and keep its temporary test database isolated.
- **SQLite reports an error:** Stop any writer, make a verified backup, inspect the configured `DATABASE_PATH`, and use SQLite read-only integrity checks before considering recovery. Never delete the database or Docker volume as a troubleshooting shortcut.
