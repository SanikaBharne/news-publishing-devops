# Week 13 - Deployment Monitoring and Verification

## Purpose

Verify the deployed Week 12 application without changing it: check the web page and health endpoint, confirm the existing Docker container is running and healthy, and inspect a short tail of its logs. These checks are read-only and do not rebuild, restart, replace, or remove the container or its `news-publishing-data` volume.

## Windows PowerShell verification

Run these commands from any PowerShell window on the host.

### Application page

```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5001/" -UseBasicParsing
"HTTP $([int]$response.StatusCode)"
```

Expected: `HTTP 200`. The page content should be returned.

### Health endpoint

```powershell
$response = Invoke-WebRequest -Uri "http://localhost:5001/health" -UseBasicParsing
"HTTP $([int]$response.StatusCode)"
$response.Content
```

Expected:

```text
HTTP 200
{"message":"News Publishing Workflow MVP running","status":"ok"}
```

### Container status and published port

```powershell
docker ps --filter "name=news-publishing-container" --format "table {{.Names}}`t{{.Status}}`t{{.Ports}}"
docker inspect --format "Name={{.Name}} State={{.State.Status}} Health={{.State.Health.Status}} Image={{.Config.Image}}" news-publishing-container
```

Expected: one `news-publishing-container` row, a status containing `Up` and `(healthy)`, and host port `5001` mapped to container port `5001`. The inspect output should say `State=running` and `Health=healthy`.

### Recent logs

```powershell
docker logs --tail 20 news-publishing-container
```

Expected: recent application access/startup entries, including successful `GET /health` requests (`200`). A `400` response to a test `POST /api/articles` can be an expected validation result; investigate repeated errors or startup/traceback messages rather than treating that single response as proof of an outage.

## Results observed on 2026-10-13

- `http://localhost:5001/` returned HTTP 200.
- `http://localhost:5001/health` returned HTTP 200 and `{"message":"News Publishing Workflow MVP running","status":"ok"}`.
- `docker ps` showed `news-publishing-container` as `Up 8 minutes (healthy)` with port `5001` published on IPv4 and IPv6.
- The last 20 container log lines included successful `/health` requests and an HTTP 200 page request. They also included a test article submission returning HTTP 400; this is an application validation response, not a container health failure.

These results are transcribed from live command output in this session. No screenshot or raw transcript was captured. The project report says the Week 12 Jenkins pipeline completed successfully; Jenkins was not rerun or independently verified in this session because the deployment checks passed and no pipeline issue required a rerun.

## Troubleshooting

- **Connection refused or timeout:** Check `docker ps --filter "name=news-publishing-container"` and confirm Docker Desktop/the Docker engine is available. If the container is not running, inspect `docker inspect` and `docker logs --tail 50 news-publishing-container` before taking action. Do not remove the container or volume as a first response.
- **Page responds but health is not HTTP 200:** Inspect the recent logs and verify that the container reports `healthy`. Preserve `news-publishing-data`; do not delete or recreate it.
- **Container is running but port 5001 is not published:** Inspect `docker port news-publishing-container`. Investigate the deployment configuration before making changes.
- **Only Jenkins verification is requested:** Review `News-Publishing-Week12-CD` in Jenkins and its latest console output. The local host checks do not establish Jenkins build status.

Do not restart or redeploy a healthy container solely to collect evidence.
