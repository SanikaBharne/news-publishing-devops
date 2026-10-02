# Week 8 – Automated Health Check

## Objective

A health check was added to verify that the application is actually running after deployment.

## Health Endpoint

The existing endpoint used for verification is:

`GET /health`

The expected successful response contains:

```json
{
  "status": "ok",
  "message": "News Publishing Workflow MVP running"
}
```

## Health Check Script

The health-check script is:

`scripts/healthcheck.py`

It checks the deployed application at:

`http://127.0.0.1:5001/health`

The script performs multiple attempts because the application may require a short amount of time to start.

The configured check uses up to **10 retries**.

## Result

The final verification produced:

```text
[PASS] Health check passed (attempt 9): {"message":"News Publishing Workflow MVP running","status":"ok"}
```

The HTTP response was:

`200 OK`

## Pipeline Behavior

If the health endpoint responds successfully, the Jenkins pipeline continues successfully.

If the health check fails after the available retries, the pipeline fails.

This ensures that a deployment is not considered successful merely because the deployment command executed.

## Week 8 Outcome

Automated post-deployment health verification was successfully implemented.