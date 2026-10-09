# Docker Build Stage

After the existing unit tests pass, Jenkins builds from the repository root:

```bat
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\verify_docker_engine.ps1
docker build -t news-publishing-app:week12 -t news-publishing-app:week12-build-%BUILD_NUMBER% .
```

The first command confirms Docker Engine is reachable and is using Linux containers, not just that the client exists. The reusable `week12` tag identifies this week's image. The build-number tag identifies the exact artifact created by a particular Jenkins run, and the deployment uses that exact tag. No image is pushed to a registry. The existing Week 11 `Dockerfile` and `.dockerignore` remain the only image configuration.

**Expected result:** Docker build succeeds and both tags refer to the new image. The Docker engine check prevents a misleading CLI-only success.

**Executed locally:** `docker build -t news-publishing-app:week12 -t news-publishing-app:week12-build-local .` completed successfully using the Docker Desktop Linux engine. Both tags were created. Jenkins itself was not run from this workspace.
