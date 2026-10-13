# Week 13 - Evidence Checklist

Save screenshots or captured command output under `docs/evidence/week-13/`. Redact credentials, tokens, and unrelated personal data before committing evidence.

- [ ] Application page open at `http://localhost:5001/`, with the successful response visible.
- [ ] PowerShell output showing `GET /` returned HTTP 200.
- [ ] PowerShell output showing `/health` returned HTTP 200 and JSON status `ok`.
- [ ] `docker ps` output showing `news-publishing-container` is `Up` and `(healthy)`, with port 5001 published.
- [ ] Recent `docker logs --tail 20 news-publishing-container` output showing successful health requests and no relevant startup failure.
- [ ] Jenkins `News-Publishing-Week12-CD` build page/console showing `Finished: SUCCESS` and the passed unit/Selenium test stages, if retaining independent Jenkins evidence.

No screenshots or raw terminal output were saved during this session. The live verification results are transcribed in `deployment-monitoring.md`; this checklist remains open until evidence is captured.
