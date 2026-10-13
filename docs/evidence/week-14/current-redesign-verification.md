# Current NewsFlow integration verification

**Checked:** 2026-10-13
**Source branch:** `feature/newsflow-ui-redesign`
**Source commit tested:** `acc13889d72955ef7d0ee888df63a9d656d0c0f5` (NewsFlow source unchanged by the documentation/pipeline integration commit)

## Local tests

Run from the redesign source checkout using the configured Windows virtual environment:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_submission.py tests\test_reviewer.py tests\test_auth_public.py -v
.\.venv\Scripts\python.exe -m pytest tests\selenium -v
```

Results: **24 backend tests passed** and **9 Selenium tests passed**. The backend tests include role checks, CSRF enforcement, draft/submission validation, review rules, mandatory rejection comments, bookmarks, and a regression proving an approved article becomes visible in the Reader edition. Selenium covers the publisher, reviewer, and reader flows.

## Authenticated Jenkins result

Jenkins `News-Publishing-Week12-CD` build **#4** completed with `SUCCESS`. The authenticated console identifies its checkout as:

```text
Checking out Revision f08f8b5d4535c52d3fffce1e818d9da69a5cc3ec
(refs/remotes/origin/feature/jenkins-docker-cd)
Commit message: "Add Jenkins Python environment check"
```

That build reported 15 unit tests and 8 Selenium tests passing, Docker build/deployment stages, and successful health checks. This is verified evidence for the Week 12 CD branch only; it does **not** validate the NewsFlow redesign commit above. The Jenkins job must be pointed at the redesign branch and run before claiming Jenkins verification for this version. No new Jenkins build was triggered.

## Live deployment

The container was rechecked on 2026-10-13. These Windows PowerShell commands are read-only:

```powershell
curl.exe --silent --show-error --max-time 8 --write-out "`nHTTP %{http_code}`n" http://127.0.0.1:5001/health
# News Publishing Workflow MVP running
# {"status":"ok"}
# HTTP 200

docker inspect news-publishing-container --format "{{.State.Status}} {{.State.Health.Status}} image={{.Image}} volumes={{range .Mounts}}{{.Name}}:{{.Destination}} {{end}}"
# running healthy image=sha256:b075a703370120c3f7e3b77421c10ae3823fe0b9258314defaf18993f2632b7a volumes=news-publishing-data:/data

docker logs --tail 20 news-publishing-container
# Recent health checks and homepage/static/API requests; no error visible in returned tail.
```

The persistent `news-publishing-data` volume remains mounted at `/data`. This image was deployed before the final regression-test/documentation integration commit. A later local candidate image (`sha256:bba1c63f9d8065453ea6e0025fc4ff07cabf77da51fe665f9c6e6f927b3511bb`) was built but not deployed; do not treat its build as a runtime or Jenkins result.

The live SQLite account table had no Reader or Publisher rows when checked previously. Accounts still need to be created interactively for a role-based demonstration.

## Evidence limitations

This file is a text record, not a screenshot or full Jenkins console archive. No screenshot evidence was captured. The original Week 12–14 evidence checklists remain unchecked where files were not actually captured.
