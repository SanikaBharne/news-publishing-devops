# Week 14 - Evidence Checklist

Store genuine screenshots or command captures under `docs/evidence/week-14/`. Redact credentials, tokens, and unrelated personal data.

## Available now

- [x] `docs/evidence/week-14/verification-results.md` — concise transcription of actual Week 14 app, Docker, Jenkins-access, UI-hash, and log checks. It is text, not a screenshot or complete raw terminal transcript.
- [x] Week 12 documentation records 15 unit and 8 Selenium tests passing. These are historical records, not Week 14 test runs.
- [x] Week 13 includes a text verification record. It is not a screenshot or independent Jenkins confirmation.
- [x] `docs/evidence/week-14/current-redesign-verification.md` — current local test counts, live health/container/volume check, and Jenkins build #4 source-branch mismatch. This is a text transcription, not screenshots or archived full output.

## Still needed for release evidence

- [ ] Screenshot of `/health` returning HTTP 200 and `status: ok` (the text result is recorded; the screenshot was not captured).
- [ ] Screenshot showing the running container, healthy status, image tag, and port mapping (a read-only container/volume check is recorded; the screenshot was not captured).
- [ ] Relevant full container log context for the Gunicorn worker abort/restart, especially if it recurs.
- [ ] Configure/run Jenkins against `feature/newsflow-ui-redesign`, then capture its build page and console with the tested revision and test results. Build #4 succeeded on the Week 12 CD branch, not this redesign branch.
- [ ] Screenshots of the deployed reader homepage, publisher dashboard/editor, and reviewer UI, with deployed image/build identification.
- [ ] Screenshot or complete saved test output for the 24 backend and 9 Selenium tests run against commit `acc1388`.

Do not mark screenshots or full logs as captured until the actual files exist in this directory. No screenshots were captured during the current verification.
