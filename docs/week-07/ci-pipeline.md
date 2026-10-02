# CI Pipeline Documentation

## Overview
The Continuous Integration (CI) pipeline automates the building and testing of the News Publishing Workflow application. It ensures that every code integration on the `development` branch is verified by an automated build.

## Pipeline Stages Execution Details
1. **Checkout**: 
   - Jenkins pulls the latest source code from the configured GitHub repository branch (`development`).
   - This ensures the build is running against the most current integrated codebase.
2. **Install Dependencies**:
   - A dedicated Python virtual environment (`venv`) is created in the Jenkins workspace to avoid conflicts with global system packages.
   - Project dependencies listed in `requirements.txt` (e.g., Flask, pytest) are installed into this isolated environment.
3. **Run Tests**:
   - The test suite (`pytest`) is invoked within the virtual environment.
   - The pipeline monitors the exit code of the test command. A zero exit code (all tests pass) allows the pipeline to succeed. A non-zero exit code (one or more tests fail) causes the pipeline to fail and abort further execution.

## Outcomes
- **SUCCESS**: Indicated by a green checkmark or blue circle in the Jenkins dashboard. Code is verified and considered healthy.
- **FAILURE**: Indicated by a red circle in the Jenkins dashboard. Code integration has introduced a regression or error, requiring developer intervention.
