# Jenkins and Docker Integration

Week 12 adds local Docker image building and container deployment to the existing Windows Jenkins pipeline. No public registry or new Jenkins credentials are needed.

The pipeline order is: Checkout, Install Dependencies, Run Unit Tests, Build Docker Image, Deploy Docker Container, Health Check, Run Selenium Tests, and Final Verification. Each test/deployment command fails the Jenkins stage when it returns an error.

The Jenkins agent must have Python, Docker CLI, a running Docker Desktop Linux engine, Selenium's browser prerequisites, and access to the repository. Docker CLI availability alone is not enough; `scripts\verify_docker_engine.ps1` checks the Linux engine as the Jenkins service account. Check the Jenkins service identity with Windows Services or:

```powershell
Get-CimInstance Win32_Service -Filter "Name='Jenkins'" | Select-Object Name, State, StartName
```

If `docker info` fails only in Jenkins, confirm Docker Desktop is running in Linux-container mode, check `docker context show` in an interactive terminal, and compare the Jenkins service's configured account with the account that can access the Docker Desktop engine. The Jenkins service account needs permission to use that engine endpoint. A machine administrator may need to configure the service to run under an authorized account and restart it; do not apply that system-level change without approval. This project does not change Windows service accounts or Docker permissions.

**Executed locally:** Docker CLI and Linux engine responded to `docker --version` and `docker info`. Existing unrelated containers and images were left unchanged. Port 5001 had no listener before this task's deployment. The Jenkins service was reported as `LocalSystem`; Jenkins-to-engine access was not tested under that service identity.
