# Jenkins Job Setup Documentation

## Overview
A new Jenkins job was created to automate the CI pipeline for the News Publishing Workflow.

## Job Configuration
1. **Name**: `news-publishing-devops-ci`
2. **Type**: Pipeline
3. **General**: Discard old builds configured to save disk space.
4. **Pipeline Definition**: `Pipeline script from SCM`
   - **SCM**: Git
   - **Repository URL**: `https://github.com/SanikaBharne/news-publishing-devops`
   - **Credentials**: None required (public repository).
   - **Branches to build**: `*/development`
   - **Script Path**: `Jenkinsfile`

## Execution Flow
Jenkins is configured to pull the `development` branch from GitHub, look for the `Jenkinsfile` in the root directory, and execute the stages defined within it.
