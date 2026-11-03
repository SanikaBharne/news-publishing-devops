# Docker Installation and Verification

Docker Desktop (or another Docker Engine) must be installed and running with Linux containers selected. This project uses the Linux `python:3.12-slim` image.

Run these commands in PowerShell:

```powershell
docker --version
docker info
```

`docker --version` prints the installed client version. `docker info` also contacts the engine and should show server details. A client version alone does not prove that the engine is available.

**Executed in this environment:** `docker --version` returned Docker version `29.3.0` (build `5927d80`). `docker info` could not connect to `dockerDesktopLinuxEngine`; Docker Desktop's Linux engine was unavailable. No image or container was built or started.

After starting Docker Desktop, rerun `docker info`. Continue only when it displays server information.
