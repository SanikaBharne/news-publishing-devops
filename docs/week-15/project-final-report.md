# NewsFlow - Project Final Report

## Introduction

NewsFlow is a 15-week academic project that combines a small news-submission and editorial-review application with a progressively developed DevOps workflow. The project emphasizes repeatable testing, CI/CD, containerization, deployment checks, and operational documentation rather than a full commercial publishing platform.

## Problem statement

Manual article review and application deployment can be inconsistent, slow, and difficult to verify. The project addresses these risks with validated article workflows, automated tests, a Jenkins pipeline, Docker packaging, a persistent SQLite data path, and health checks.

## Objectives

- Accept article submissions and reject missing or whitespace-only required fields.
- Let a separate editorial account review a submission, approve it, or reject it with a required comment.
- Track status and expose approved stories to readers.
- Automate backend and browser tests and document the CI/CD and deployment workflow.
- Preserve existing SQLite data when applying the additive schema and container deployment model.

## Technology stack

| Area | Technology |
|---|---|
| Backend | Python, Flask |
| UI | Jinja templates, HTML, CSS, vanilla JavaScript |
| Persistence | SQLite |
| Authentication | Flask sessions, Werkzeug password hashes, role checks, CSRF tokens |
| Tests | pytest, Selenium, headless Chrome |
| Windows local serving | Waitress |
| Container runtime | Docker, Python 3.12 slim image, Gunicorn, non-root application user |
| CI/CD | Declarative Jenkins pipeline on a Windows agent |
| Source control | Git and GitHub feature branches/pull requests |

## System architecture

```text
Reader / Publisher browser
        |
        | HTTP pages and JSON API
        v
Flask application (Jinja + static CSS/JavaScript)
        |
        v
SQLite database
        ^
        | Docker: /data/app.db backed by named volume
        |
Jenkins -> checkout -> Python setup -> pytest -> Docker build
        -> container deployment -> health check -> Selenium -> final verification
```

Locally on Windows, `scripts/deploy.py` serves the Flask application with Waitress on port 5001 by default. The Docker image serves it with Gunicorn on container port 5001 and defines a `/health` check. The Jenkins pipeline uses the existing project volume `news-publishing-data` for SQLite persistence.

## Implementation

The application supports:

- Publisher drafts, preview, submission, and dashboard.
- Required-field validation on the server and in the browser; whitespace-only submissions are rejected.
- A reviewer queue and `SUBMITTED` → `APPROVED` / `REJECTED` transitions.
- Mandatory non-whitespace rejection comments and review status/detail APIs.
- Reader access to approved stories, public search/category filtering, and saved-story bookmarks.
- Hashed passwords, server-side role checks, CSRF protections, and restrictions against self-review.

Reader and Publisher are the account roles. Editorial review is performed by a second Publisher account, not by a distinct reviewer role. Accounts are provisioned interactively; public account registration is not implemented. Existing article API routes and status values remain compatible. The public edition exposes approved articles only.

SQLite setup is additive: the application creates user/bookmark tables and adds optional article columns. The Week 15 check opened the local database read-only and found it integrity-valid with 33 article rows. The database and its secret file were not modified by the Week 15 test runs.

## CI/CD workflow

The existing Jenkinsfile contains Checkout, Check Python, Install Dependencies, Run Unit Tests, Build Docker Image, Deploy Docker Container, Health Check, Run Selenium Tests, and Final Verification stages. The Docker deployment script checks project ownership, tests a candidate image, uses the named SQLite volume, performs health checks, and includes rollback handling.

This pipeline was inspected but **not executed in Week 15**: Jenkins at `127.0.0.1:8080` did not respond and Docker Engine was unavailable. The deploy step can replace the existing container, so it must only be run in an authorized deployment environment. Historical Jenkins results are not treated as Week 15 validation.

## Testing strategy and Week 15 results

Backend tests cover submission, validation, review decisions, status tracking, authentication, authorization, CSRF, public visibility, bookmarks, and cross-role publishing. Selenium tests cover publisher, reviewer, and reader journeys using an isolated temporary database and browser.

- Backend: **24 passed, 0 failed, 0 skipped** in 15.25 seconds.
- Selenium: **9 passed, 0 failed, 0 skipped** in 62.44 seconds.
- A separate integration suite is not present; a cross-role approval-to-reader regression is included in the backend suite.
- The local `app.db` SQLite integrity check passed. A live application on port 5001 was unavailable; Selenium's isolated test server passed its startup health check.

Detailed execution information is in the [final testing report](final-testing-report.md).

## Deployment process

The documented release path is: install Python dependencies, run backend tests, build the existing Dockerfile, deploy with the project PowerShell helper and existing named volume, verify container health and `/health`, and run Selenium against the deployed endpoint.

Week 15 did not build or start a container because Docker Desktop's Linux engine named pipe was unavailable. Therefore the Week 15 image build, current container state/logs, Docker health, and persistence across a restart/replacement remain unverified. The project is not declared fully deployment-validated.

## Results

The application behavior is covered by 33 passing automated tests, including browser-driven submission, review, reader, and validation flows. The on-disk SQLite database passed a read-only integrity check. Final documentation and an explicit pending-evidence checklist were prepared.

The available evidence does **not** establish a current Jenkins build or Docker deployment. The final release gate remains open until those services are available and actual results are recorded.

## Benefits

- Repeatable tests catch regressions in API, role-based access, and user workflows.
- Status tracking and required rejection feedback support a clear editorial process.
- Isolated Selenium data reduces the risk of changing project data during UI tests.
- Docker's named volume separates persisted SQLite data from the replaceable application container.
- Pipeline-as-code documents the build, test, deployment, and health-check sequence.

## Limitations

- No Week 15 Jenkins run or Docker build/deployment was possible in the checked environment.
- There is no separate integration-test suite; integration coverage is embedded in pytest and Selenium scenarios.
- The existing deployment targets fixed container/volume names and is not safe to invoke casually against a live deployment.
- Editorial reviewers share the Publisher role; there is no public registration or standalone review role.
- Screenshot evidence is not present, and no Week 15 pull request has yet been created or merged.
- Ansible/Puppet provisioning, cloud deployment, and Kubernetes are not implemented.

## Future enhancements

- Run the pipeline on a correctly configured Jenkins agent against an approved isolated deployment target.
- Capture genuine Jenkins, Docker, health, and application screenshots and attach the build/test logs.
- Add a separate integration-test entry point only if it improves coverage beyond existing end-to-end scenarios.
- Add infrastructure provisioning and a dedicated editorial-review role if required by future scope.
- Add production-grade external secret management, HTTPS, backup/restore drills, and deployment observability before production use.

## Conclusion

NewsFlow meets its core application objectives and passed all locally executable Week 15 backend and Selenium tests. The local SQLite file is integrity-valid and was preserved. Because Jenkins and Docker were unavailable, release readiness is conditional: the CI/CD run, container lifecycle, deployed health, and screenshot evidence must still be verified before calling the project fully released.
