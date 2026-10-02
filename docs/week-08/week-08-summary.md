# Week 8 – Summary

## Objective

Week 8 focused on extending the Jenkins CI pipeline into a basic deployment workflow using Pipeline as Code and automated server deployment.

## Work Completed

* Updated the root-level `Jenkinsfile`.
* Added five Jenkins pipeline stages:

  * Checkout
  * Install Dependencies
  * Run Tests
  * Deploy Application
  * Health Check
* Added `scripts/deploy.py`.
* Added `scripts/healthcheck.py`.
* Added Waitress for Windows-compatible WSGI deployment.
* Added Gunicorn to the requirements as part of the deployment setup.
* Configured deployment on port `5001`.
* Added automated health verification.
* Configured the pipeline to fail when the health check fails.
* Verified the existing 14-test suite.

## Verification Results

```text
14 passed, 13 warnings in 0.73s
```

Deployment health check:

```text
[PASS] Health check passed (attempt 9)
HTTP 200 OK
```

Git commit:

```text
349f532 ci: add Jenkins deployment and health check
```

Feature branch:

```text
feature/pipeline-server-deployment
```

Working tree:

```text
nothing to commit, working tree clean
```

## Week 8 Milestone Status

* Week 1–3: Problem Definition, Agile Planning, Requirements and Architecture ✅
* Week 4: Git & GitHub Setup ✅
* Week 5: Article Submission API and Validation ✅
* Week 6: Reviewer Workflow, Approval, Rejection and Status Tracking ✅
* Week 7: Jenkins Installation and Basic CI ✅
* Week 8: Pipeline as Code and Server Deployment ✅

## Scope Control

The following technologies were intentionally not introduced in Week 8:

* Selenium
* Docker
* Ansible
* Kubernetes

They remain planned for their respective later weeks.

## Conclusion

Week 8 successfully extended the project's Jenkins pipeline from basic continuous integration to automated application deployment and post-deployment health verification. The application was deployed on port `5001`, all existing tests passed, and the live health endpoint returned HTTP 200.