# Docker Image Build

From the repository root, confirm Docker Engine is available with `docker info`. Then build the image:

```powershell
docker build -t news-publishing-app:week11 .
docker images
```

The first command builds and tags this project's image. The second lists local images; look for `news-publishing-app` with tag `week11`.

**Expected outcome (not executed):** the build completes without errors and the tagged image appears in `docker images`.

**Actual result:** image build was not attempted because `docker info` could not connect to the Docker Desktop Linux engine. The image is not claimed to exist.
