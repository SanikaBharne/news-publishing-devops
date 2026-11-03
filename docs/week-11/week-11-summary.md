# Week 11 - Summary

## Objective

Package the existing News Publishing Workflow Flask app in a Docker image and document the image and container lifecycle, without adding Docker deployment to Jenkins.

## Implemented

- Added a root Dockerfile using Python 3.12 slim, Gunicorn, a non-root runtime user, port 5001, and a Python-based `/health` check.
- Added `.dockerignore` so local artifacts and development-only files are not sent in the build context.
- Added a backward-compatible `DATABASE_PATH` override and documented a named volume at `/data` for SQLite.
- Added guides for image building, container lifecycle, port mapping, health checks, persistence, tests, branch workflow, and evidence.

## Verification and limitations

- Unit tests: 15 passed, including a check of the configurable database path.
- Local Flask `/health`: HTTP 200 with expected JSON.
- Host port 5001: no listener found at check time.
- Docker client: available; Docker Engine: unavailable. No Docker image or container lifecycle step is claimed as executed.
- Screenshots have not been captured or added.

Docker-based validation remains to be performed after Docker Desktop's Linux engine is started. Week 12 Jenkins-Docker deployment and Week 13 configuration management are out of scope.
