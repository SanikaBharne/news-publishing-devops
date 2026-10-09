# Container Deployment

Jenkins runs `scripts\deploy_docker.ps1` after the image build:

```bat
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\deploy_docker.ps1 -Image "news-publishing-app:week12-build-%BUILD_NUMBER%" -ContainerName "news-publishing-container" -VolumeName "news-publishing-data" -HostPort 5001 -BuildId "%BUILD_NUMBER%"
```

The script starts the exact image from this build, maps host port `5001` to container port `5001`, sets `DATABASE_PATH=/data/app.db`, and mounts the named SQLite volume `news-publishing-data:/data`. It adds the project label `com.news-publishing.project=news-publishing-devops` to containers it creates. A previously-created Week 11 container using the known `news-publishing-app:*` image is also recognized.

Before deployment, it verifies Docker, checks for other containers publishing port 5001, checks Windows host listeners, and confirms an existing named container is identifiable as this project. It starts an isolated image candidate and waits for its Docker health check before replacing the running deployment.

**Verified locally:** the helper deployed the image twice, including a replacement of the first running container. The new container became healthy, `/health` returned the expected response, and an article created before replacement remained available afterward. `news-publishing-container` is left running on port 5001 with `news-publishing-data` mounted.
