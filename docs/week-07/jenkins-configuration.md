# Jenkins Configuration Documentation

## Overview
After installation, Jenkins required specific global configuration and plugin setups to integrate with the News Publishing Workflow project (Python, Git, GitHub).

## Global Security and Tool Configuration
1. **Manage Jenkins > Global Tool Configuration**:
   - **Git**: Ensured the path to the Git executable is correctly identified by Jenkins (usually `git.exe` on Windows if in PATH).
   - **Python**: Verified that Python 3 is accessible to the Jenkins agent. In a local Windows environment, Python is accessed via the system PATH.

## Plugins
The standard "suggested plugins" bundle installed during setup provides the required capabilities:
- **Git Plugin**: Allows Jenkins to clone the repository.
- **Pipeline**: Enables Jenkins to read and execute the `Jenkinsfile`.
- **Pipeline: GitHub**: Integrates the pipeline with GitHub repositories.

No additional, unnecessary plugins (like Docker or Ansible) were installed during Week 7, preserving a clean and focused environment.
