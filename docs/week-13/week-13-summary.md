# Week 13 - Summary

## Objective

Perform a small, non-disruptive verification of the Week 12 CI/CD deployment and document repeatable monitoring checks and evidence requirements.

## Tasks completed

- Reviewed the Week 12 summary, Jenkins/Docker integration notes, and test/deployment results.
- Checked the application root and `/health` endpoint on `localhost:5001`.
- Checked the running Docker container and its published port, and reviewed its recent logs.
- Added deployment monitoring instructions, expected output, troubleshooting guidance, and an evidence checklist.
- Kept the application, database volume, and Jenkins pipeline unchanged. No pipeline rerun was needed based on the successful local deployment checks and the reported Week 12 Jenkins success.

## Verification results

- Application root: HTTP 200.
- Health endpoint: HTTP 200; status `ok`.
- Docker: `news-publishing-container` was `Up 8 minutes (healthy)` with port 5001 published.
- Recent logs: successful health/page requests were present. A test article POST returned HTTP 400; no health failure was indicated by the observed output.
- Jenkins: Week 12 success is reported in the project status supplied for this task, but the latest build was not independently checked during this session.
- Tests: no unit or Selenium test suite was rerun; Week 13's executed checks were read-only deployment checks.
- Screenshots: none captured.

## Conclusion

The application was reachable and healthy during this verification. The existing container and persistent volume were left intact. Capture the requested Jenkins and deployment evidence separately if needed; do not represent screenshots or a fresh Jenkins build as completed until captured or verified.
