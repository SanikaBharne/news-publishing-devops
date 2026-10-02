# Project-Specific DevOps Workflow

Below is the detailed workflow planned for the News Publishing Workflow project. 

*Note: Stages from Jenkins onwards will be implemented progressively in later weeks (Week 7-14).*

1. **Developer**: Writes code for the application or updates configuration files locally.
2. **Feature Branch**: Code is committed to a local Git branch.
3. **Commit**: Changes are saved securely in version control.
4. **GitHub**: Code is pushed to the central remote repository.
5. **Pull Request/Review**: Code is reviewed before merging.
6. **Main/Development Branch**: Code is merged into the primary branch.
7. **Jenkins** *(Week 7+)*: A webhook or poll triggers the CI orchestration server.
8. **Build** *(Week 7+)*: Source code is compiled and prepared.
9. **Test** *(Week 9-10+)*: Automated Selenium tests validate functionality.
10. **Quality Gate** *(Week 10+)*: If tests fail, the pipeline halts immediately.
11. **Package** *(Week 11+)*: The application is packaged into a deployable artifact.
12. **Docker** *(Week 11-12+)*: The artifact is built into a container image.
13. **Deployment** *(Week 12-14+)*: Jenkins deploys the Docker container to a server provisioned by Ansible/Puppet.
14. **Health Check** *(Week 14+)*: The pipeline verifies the application is up and running.
15. **Operations/Feedback**: The developer is notified of the pipeline's success or failure.
