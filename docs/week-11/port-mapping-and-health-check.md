# Port Mapping and Health Check

The Flask service listens on container port `5001`. The recommended run option `-p 5001:5001` exposes it on host port `5001`, so open:

- Homepage: `http://localhost:5001/`
- Health endpoint: `http://localhost:5001/health`

Before starting the container, check host port 5001 in PowerShell:

```powershell
Get-NetTCPConnection -LocalPort 5001 -State Listen -ErrorAction SilentlyContinue
```

If this prints a listener, identify the owner before proceeding; do not stop an unrelated process. If you need a different available host port, for example `5002`, map `-p 5002:5001` and use `http://localhost:5002/` and `http://localhost:5002/health`. The container port stays 5001.

The Dockerfile health check calls `/health` with Python's standard library. Check its status with:

```powershell
docker inspect --format="{{.State.Health.Status}}" news-publishing-container
```

The status should become `healthy` after startup. A direct response can also be checked with:

```powershell
(Invoke-WebRequest http://localhost:5001/health).StatusCode
(Invoke-WebRequest http://localhost:5001/health).Content
(Invoke-WebRequest http://localhost:5001/).StatusCode
```

**Actually verified locally:** Flask's test client returned HTTP 200 from `/health` and JSON `{"message":"News Publishing Workflow MVP running","status":"ok"}`. Host port 5001 had no listener at the time of checking. Container health and browser access remain unverified because Docker Engine is unavailable.
