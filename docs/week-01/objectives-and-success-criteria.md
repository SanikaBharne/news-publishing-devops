# Objectives and Success Criteria

## Application Objectives
- Build a functional, simple, monolithic News Publishing Workflow application.
- Track an article from submission through the review process to final approval or rejection.
- Maintain a minimal application scope to prioritize DevOps implementation.

## DevOps Objectives
- Progressively implement a complete CI/CD pipeline utilizing industry-standard tools.
- Automate source code management using Git and GitHub.
- Automate application build and testing processes using Jenkins and Selenium.
- Containerize the application for consistent deployment using Docker.
- Automate the provisioning and configuration of target deployment servers using Ansible or Puppet.

## Measurable Success Criteria

| Criterion | Type | How it will be verified |
|---|---|---|
| **Application MVP Completion** | Application | Verify that a writer can submit an article and an editor can approve or reject it (with a comment), with status tracking updating correctly. |
| **Automated CI/CD Pipeline** | DevOps | A successful code change should be able to pass through automated build, testing and deployment stages in Jenkins with deployment blocked when automated tests fail. Verified by demonstrating a commit triggering a pipeline run. |
| **Infrastructure as Code** | DevOps | Configuration management tools (Ansible/Puppet) can consistently provision the deployment environment from scratch. Verified by destroying the target environment and running the configuration scripts to rebuild it. |
