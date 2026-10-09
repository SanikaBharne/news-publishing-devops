# Container Lifecycle

Run commands from the repository root in PowerShell after building the image. First check that the name is not already in use:

```powershell
docker ps -a --filter "name=^news-publishing-container$"
docker image inspect news-publishing-app:week11
docker volume inspect news-publishing-data
```

An image or volume inspection may return an error when that name is not yet present. If any named resource already exists, verify that it belongs to this Week 11 exercise before reusing or replacing it; otherwise choose a unique name and update the commands. Do not remove resources from another project. If a container with that name is listed, do not remove or replace it unless you have verified that it is this Week 11 container and no longer needed. Create persistent storage and start this container:

```powershell
docker volume create news-publishing-data
docker run -d --name news-publishing-container -p 5001:5001 -v news-publishing-data:/data -e DATABASE_PATH=/data/app.db news-publishing-app:week11
```

`-d` runs in the background, `--name` gives the container a clear name, `-p 5001:5001` maps host port 5001 to container port 5001, and the named volume stores SQLite data outside the container.

Use these commands to inspect it:

```powershell
docker ps
docker ps -a
docker inspect news-publishing-container
docker logs news-publishing-container
docker logs -f news-publishing-container
docker inspect --format="{{.State.Health.Status}}" news-publishing-container
```

The first two list running containers and all containers, including stopped ones. `inspect` displays configuration and runtime details. `logs` shows recent output; `logs -f` follows new output until you press Ctrl+C. The formatted inspect command should eventually print `healthy`.

Lifecycle commands:

```powershell
docker stop news-publishing-container
docker start news-publishing-container
docker restart news-publishing-container
docker stop news-publishing-container
docker rm news-publishing-container
docker rmi news-publishing-app:week11
```

Stop pauses the running container. Start resumes a stopped container; restart stops and starts it. Remove the container only after it is stopped. Remove the image only after its container is removed. These commands have not been executed here because the engine is unavailable. Keep `news-publishing-data` if you want to preserve articles; removing a container does not remove the volume.
