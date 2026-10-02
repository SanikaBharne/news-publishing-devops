# Week 8 – Testing and Verification

## Automated Testing

The existing pytest test suite was executed before deployment.

Result:

```text
14 passed, 13 warnings in 0.73s
```

All 14 existing tests passed successfully.

No tests were added or modified during Week 8.

## Deployment Verification

After successful testing, the application was deployed on port `5001`.

The deployment was verified using the health-check script.

Endpoint:

```text
http://127.0.0.1:5001/health
```

Result:

```text
HTTP 200 OK
```

Health response:

```text
[PASS] Health check passed (attempt 9)
```

## Git Verification

Feature branch:

```text
feature/pipeline-server-deployment
```

Commit:

```text
349f532 ci: add Jenkins deployment and health check
```

Git status:

```text
nothing to commit, working tree clean
```

## Files Changed

The following files were changed or added:

* `Jenkinsfile`
* `requirements.txt`
* `scripts/deploy.py`
* `scripts/healthcheck.py`

## Overall Verification

The Week 8 implementation successfully passed the automated test suite, deployed the application, and verified the running application through the health endpoint.