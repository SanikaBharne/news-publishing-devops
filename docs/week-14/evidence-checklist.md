# Week 14 - Evidence Checklist

Store genuine screenshots or command captures under `docs/evidence/week-14/`. Redact credentials, tokens, and unrelated personal data.

## Available now

- [x] `docs/evidence/week-14/verification-results.md` — concise transcription of actual Week 14 app, Docker, Jenkins-access, UI-hash, and log checks. It is text, not a screenshot or complete raw terminal transcript.
- [x] Week 12 documentation records 15 unit and 8 Selenium tests passing. These are historical records, not Week 14 test runs.
- [x] Week 13 includes a text verification record. It is not a screenshot or independent Jenkins confirmation.

## Still needed for release evidence

- [ ] Screenshot or complete PowerShell output showing `/health` HTTP 200 and the healthy response body.
- [ ] Screenshot showing the running container, healthy status, image tag, and port mapping.
- [ ] Relevant full container log context for the Gunicorn worker abort/restart, especially if it recurs.
- [ ] Authenticated Jenkins latest-build page and console showing the build number, `Finished: SUCCESS`, and actual test-stage results.
- [ ] After UI integration and deployment, screenshot of both the submission page and reviewer UI showing the redesign, plus deployed image/build identification.
- [ ] Fresh unit and Selenium test output from the validated UI revision.

Do not mark evidence as captured until the actual file exists in this directory. No screenshots or full logs were captured during Week 14.
