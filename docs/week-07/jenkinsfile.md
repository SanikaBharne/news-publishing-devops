# Jenkinsfile Documentation

## Overview
The `Jenkinsfile` defines the Continuous Integration pipeline as Code (PaC). It resides in the root of the project repository and is automatically executed by Jenkins upon triggering a build.

## Structure and Syntax
The pipeline uses Declarative Pipeline syntax, which provides a structured and readable format.

### Key Sections
1. **Agent**: `agent any` instructs Jenkins to execute the pipeline on any available executor.
2. **Stages**: Contains the sequence of steps to be executed.
   - **Checkout**: `checkout scm` uses the Git plugin to pull the source code from the configured repository branch.
   - **Install Dependencies**: Executes a Windows batch script (`bat`) to create a Python virtual environment (`venv`), activate it, and install required packages via `pip install -r requirements.txt`.
   - **Run Tests**: Executes the `pytest` test suite within the activated virtual environment using `python -m pytest -v`.
3. **Post Actions**:
   - `always`: Logs a completion message regardless of outcome.
   - `success`: Logs a specific success message when all stages complete successfully (i.e., all 14 tests pass).
   - `failure`: Logs a failure message if any stage, particularly the test stage, exits with a non-zero code.

## Operating System Considerations
The `bat` command is used specifically because Jenkins is installed on a Windows development machine. In a Linux/Unix environment, `sh` would be used instead.
