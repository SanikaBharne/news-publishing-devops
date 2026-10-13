# Week 14 - Final Validation

## Scope and safety

Checks were run from Windows PowerShell on 2026-10-13. The app, container, image, and `news-publishing-data` volume were not changed. No tests, image build, redeployment, or Jenkins build were started.

## Application and container checks

Run from any PowerShell window on the Windows host:

```powershell
curl.exe --silent --show-error --max-time 4 --write-out "`nHTTP %{http_code}`n" http://localhost:5001/health
curl.exe --silent --show-error --max-time 4 http://localhost:5001/ | Select-String -Pattern '<title>|<h1>'
docker ps --filter "name=news-publishing-container" --format "table {{.Names}}`t{{.Status}}`t{{.Image}}`t{{.Ports}}"
docker inspect --format "Image={{.Config.Image}} ImageID={{.Image}} State={{.State.Status}} Health={{.State.Health.Status}} Started={{.State.StartedAt}}" news-publishing-container
docker logs --tail 12 news-publishing-container
```

Observed:

- `/health` returned HTTP 200 and `{"message":"News Publishing Workflow MVP running","status":"ok"}`.
- `/` returned the current page title `Submit News Article` and heading `Submit a News Article`.
- Docker reported `news-publishing-container` as `Up 28 minutes (healthy)`, using `news-publishing-app:week12-build-4`, with host port 5001 mapped to container port 5001 on IPv4 and IPv6.
- Inspect reported `State=running`, `Health=healthy`, and image ID `sha256:99b7fda1ab197159424b64f5391872438dd6d999a50a30f94002a27537f8b8a9`. The `news-publishing-app:week12` and `news-publishing-app:week12-build-4` tags resolved to that same image ID.
- The recent log tail included successful `/health` and `/` requests. It also included a Gunicorn worker `SystemExit`/exit followed by a replacement worker boot at `2026-10-13 02:55:10 +0000`. The container remained healthy and served requests afterward; the cause of this worker abort was not established. Investigate if it recurs.

The concise command record is in `docs/evidence/week-14/verification-results.md`; no screenshot or full raw log was captured.

## UI image check

The running image's UI template hashes were compared with the checked-out source using:

```powershell
docker exec news-publishing-container sha256sum /app/src/templates/index.html /app/src/templates/reviewer.html
Get-FileHash src\templates\index.html,src\templates\reviewer.html -Algorithm SHA256
```

Both pairs matched exactly:

```text
index.html   fd21cf830c872e16a989a7d9996f653d28f92693526f618a429747b8aa6f1117
reviewer.html ea0a62d6597bd345406ff707ea437f0349eb511487a3773538771dc28307df4e
```

This proves that the image contains the templates from the currently checked-out Week 13/14 branch. It does **not** prove that it contains the separate newsroom redesign: local branch `feature/newsflow-ui-redesign` has commit `a21d699` and adds redesigned templates and static CSS/JavaScript, while that branch is not an ancestor of the current branch. The running page title/heading are the existing `Submit News Article` UI, not the redesigned `Newsflow | Newsroom Desk` title.

`Dockerfile` copies `src/` into `/app/src/`, so an image built from a source revision that does not include the redesign cannot serve that redesign. Do not rebuild or redeploy from the current branch expecting the redesign. Safest next step: review and integrate the UI branch into the intended deployment/release branch, validate it and its tests, then use the existing candidate-health/deploy pipeline. That deployment script preserves the named database volume and has rollback logic; do not remove or recreate `news-publishing-data`.

## Existing test and Jenkins records

- Week 12 `testing-and-deployment-results.md` records 15 unit tests and 8 Selenium tests passing, along with successful local Docker build/deployment and health checks. These are **previously recorded results**, not tests rerun in Week 14.
- Week 12 docs also record a Jenkins run that stopped because Python was unavailable. Week 13 documentation reports a successful Jenkins run based on supplied project status, but says it was not independently checked. These records conflict.
- The Week 14 unauthenticated request to `http://localhost:8080/job/News-Publishing-Week12-CD/lastBuild/api/json` returned HTTP 403 (`Authentication required`). Jenkins build status could not be independently confirmed. No Jenkins build was started.
- No test suites were rerun during Week 14.

To confirm Jenkins, sign in to `http://localhost:8080`, open **News-Publishing-Week12-CD**, then open the latest build and console output. Record the build number, result, and actual test-stage summaries; do not infer success from the local health check.
