# Week 12 - Summary

## Objective

Integrate the existing Linux Docker image with the Windows Jenkins pipeline to automatically build, deploy, health-check, and Selenium-test the News Publishing Workflow application.

## Implementation

- Jenkins retains checkout, dependency installation, and unit tests, then builds both a stable `news-publishing-app:week12` tag and a per-build tag.
- A Windows PowerShell deployment helper tests the candidate image, verifies ownership before replacement, persists SQLite data in `news-publishing-data`, checks health, and attempts rollback on deployment failure.
- Selenium uses configurable `APP_BASE_URL`; Jenkins points it at the Docker deployment and no longer starts the separate Waitress deployment.
- The pipeline leaves the successful application container running and reports deployment details.

## Verification

- 15 unit tests passed.
- Docker image build and two local container deployments succeeded.
- Container health and `/health` returned the expected successful response.
- Selenium: all eight existing end-to-end tests passed against the Docker deployment.
- Article data persisted through container replacement using the named volume.
- The latest supplied Jenkins run failed before tests or Docker stages because Python was not available on the Jenkins service `PATH`; the remaining stages were skipped. Ensure Python is available on the system `PATH` for the Jenkins service account, restart Jenkins, and rerun. Docker engine access under the Windows `LocalSystem` service identity also remains unverified.
- No screenshots have been captured; see the unchecked evidence checklist.

Ansible, Kubernetes, cloud provisioning, and new application features remain out of scope.
