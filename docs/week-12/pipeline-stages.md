# Pipeline Stages

The Windows Jenkins pipeline uses `bat` for Windows commands and these stages:

| Stage | Main commands | Purpose |
|---|---|---|
| Checkout | `checkout scm` | Uses the job's configured SCM branch. |
| Install Dependencies | Create `venv`, then `pip install -r requirements.txt` | Install Flask, pytest, Selenium, and existing WSGI dependencies. |
| Run Unit Tests | `python -m pytest tests\test_submission.py tests\test_reviewer.py -v` | Validate application and database behavior before image build. |
| Build Docker Image | `verify_docker_engine.ps1`, then `docker build -t news-publishing-app:week12 -t news-publishing-app:week12-build-%BUILD_NUMBER% .` | Require a running Linux engine, then build and identify the deployment artifact. |
| Deploy Docker Container | `powershell.exe ... scripts\deploy_docker.ps1` | Safely replace the named application container and keep the SQLite volume. |
| Health Check | `python scripts\healthcheck.py ...`, then `verify_container.ps1` | Verify external HTTP response and Docker runtime health. |
| Run Selenium Tests | `python -m pytest tests\selenium -v` | Exercise the Docker deployment through its host URL. |
| Final Verification | `verify_container.ps1`, healthcheck, deployment summary | Confirm it remains healthy and print the deployed image/container. |

The failure handler gathers logs for a verified project container and leaves a healthy deployment running after success. It does not kill host processes or clean up unrelated Docker resources.
