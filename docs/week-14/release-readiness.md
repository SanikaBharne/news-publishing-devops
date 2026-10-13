# Week 14 - Release Readiness

Status reflects the checks performed on 2026-10-13. “Previously recorded” results are not new Week 14 executions.

| Area | Status | Basis / action |
|---|---|---|
| Application | **Pass for current deployment** | `/health` and `/` returned HTTP 200; current UI title and heading were visible. |
| Docker | **Pass with follow-up** | Named container is running and healthy on port 5001. Recent logs show a Gunicorn worker abort/exit followed by a replacement worker; inspect for recurrence. |
| UI release | **Not ready for redesign** | Deployed template hashes match the current branch, but not the separate `feature/newsflow-ui-redesign` branch (`a21d699`). Integrate and validate the redesign before claiming it is deployed. |
| Tests | **Previously recorded pass; not rerun** | Week 12 results document 15 unit and 8 Selenium tests passing. Week 14 executed no tests. |
| Jenkins | **Unconfirmed** | Jenkins API returned 403 without authentication. Week 12 documentation reports an earlier Python failure; Week 13 records success as user-supplied but not independently verified. Confirm latest build in the authenticated UI. |
| Git | **Week 14 branch in progress** | `feature/week14-release-readiness` was created from `9a48d22`; Week 14 docs are to be committed locally. No Week 14 push or merge has been performed. |
| Documentation / evidence | **Documentation added; screenshots pending** | Week 14 validation/readiness docs and a text transcript are included. No new screenshots or full raw logs were captured. |

## Release decision

The currently running Week 12 image is serving a healthy app, but the release is **not fully verified as containing the latest UI redesign**, and latest Jenkins success is **not independently confirmed**. Treat this as a healthy existing deployment, not approval to release the UI redesign.

Before release:

1. Review and integrate the UI redesign branch into the intended deployment branch.
2. Run the relevant unit and Selenium tests and confirm the result.
3. Build/deploy through the existing pipeline and verify the served UI, health endpoint, and container.
4. Confirm the latest Jenkins build in an authenticated session and capture genuine evidence.
5. Preserve `news-publishing-data`; do not delete it during validation or redeployment.

The observed Gunicorn worker abort was followed by a new worker and healthy checks. If it appears repeatedly, investigate the complete logs before release; this check did not establish its cause.
