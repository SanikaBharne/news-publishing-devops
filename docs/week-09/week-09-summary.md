# Week 9 – Summary

## Objective

Week 9 focused on implementing Selenium-based local end-to-end testing for the News Publishing Workflow application.

## Work Completed

* Added Selenium to `requirements.txt`.
* Created a dedicated `tests/selenium/` directory.
* Created a headless Chrome WebDriver fixture.
* Created eight Selenium end-to-end tests.
* Tested article submission.
* Tested reviewer dashboard functionality.
* Tested article approval.
* Tested article rejection with a comment.
* Tested required-field validation.
* Verified that existing unit tests continued to pass.
* Used the local deployment on port `5001`.
* Committed and pushed the implementation using a feature branch.

## Verification Results

Selenium:

```text
8 passed in 16.70s
```

Existing unit tests:

```text
14 passed in 0.69s
```

Git branch:

```text
feature/selenium-local-testing
```

Commit:

```text
5caa070 test: add Selenium local end-to-end tests
```

Git status:

```text
nothing to commit, working tree clean
```

## Project Milestone Status

* Week 1–3: Problem Definition, Agile Planning, Requirements and Architecture ✅
* Week 4: Git & GitHub Setup ✅
* Week 5: Article Submission API and Validation ✅
* Week 6: Reviewer Workflow, Approval, Rejection and Status Tracking ✅
* Week 7: Jenkins Installation and Basic CI ✅
* Week 8: Pipeline as Code and Server Deployment ✅
* Week 9: Selenium Local End-to-End Testing ✅

## Scope Control

The following were intentionally not implemented in Week 9:

* Jenkins Selenium integration
* Docker
* Ansible
* Kubernetes
* New application features

Jenkins integration for automated Selenium testing is planned for Week 10.

## Conclusion

Week 9 successfully introduced browser-based end-to-end testing to the project. Eight Selenium tests covering the major user workflows passed successfully, while all 14 existing unit tests remained successful. The implementation was committed and pushed to the `feature/selenium-local-testing` branch.