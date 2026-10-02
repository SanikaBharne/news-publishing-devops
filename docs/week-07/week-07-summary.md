# Week 7 Summary – Jenkins Continuous Integration Pipeline

## Objective
The primary goal of Week 7 was to transition from manual testing to an automated Continuous Integration (CI) process by setting up Jenkins and creating a foundational CI pipeline for the News Publishing Workflow.

## Accomplishments
1. **Jenkins Infrastructure**:
   - Installed and configured a Jenkins automation server.
   - Configured necessary integrations for Git and Python.
2. **Pipeline as Code**:
   - Created a declarative `Jenkinsfile` at the repository root.
   - Defined pipeline stages:
     - **Checkout**: Pulls the `development` branch from GitHub.
     - **Install Dependencies**: Sets up a Python virtual environment and installs `requirements.txt`.
     - **Run Tests**: Executes the `pytest` test suite to verify application integrity.
3. **Automated Verification**:
   - The Jenkins pipeline successfully executed all 14 MVP unit tests.
   - Verified that the pipeline correctly reports build SUCCESS.
4. **Git Collaboration**:
   - Work was completed on the `feature/jenkins-ci` branch and successfully merged into `development`, ensuring CI is now active on the main integration branch.

## Status
The project now benefits from automated build verification, a critical milestone in establishing the full DevOps lifecycle. Week 7 tasks are fully complete.
