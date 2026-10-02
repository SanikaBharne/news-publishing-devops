# CI Testing Documentation

## Overview
This document details the testing phase executed within the Jenkins Continuous Integration pipeline.

## Testing Framework
The pipeline utilizes `pytest`, the standard testing framework adopted for this project during MVP development.

## Pipeline Integration
In the `Run Tests` stage of the `Jenkinsfile`, the command `python -m pytest -v` is executed.

## Current Test Status
- **Total Tests**: 14
- **Test Suite Components**:
  - **Submission Workflow** (`tests/test_submission.py`): 6 tests covering article creation, required-field validation, and database persistence.
  - **Reviewer Workflow** (`tests/test_reviewer.py`): 8 tests covering dashboard listing, approval logic, rejection logic (with mandatory comment validation), status transitions, and error handling for invalid requests.
- **Outcome**: The CI pipeline successfully executed all 14 tests, resulting in a 100% pass rate. This verifies the integrity of the MVP features when executed in the automated Jenkins environment.
