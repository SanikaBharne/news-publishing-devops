# Week 8 – Server Deployment

## Objective

The objective was to deploy the News Publishing Workflow application automatically after successful testing.

## Deployment Method

The application is deployed locally on port:

`5001`

The deployment script is:

`scripts/deploy.py`

The script starts the Flask application using **Waitress**, a Windows-compatible WSGI server.

## Why Waitress Was Used

Gunicorn was added to `requirements.txt` as part of the deployment setup. However, Gunicorn requires POSIX-specific functionality and cannot run directly on Windows.

Therefore, Waitress was selected as the actual WSGI runtime for the Windows Jenkins environment.

This allows the application to run as a proper WSGI application without requiring a Linux environment.

## Deployment Flow

The deployment process is:

1. Jenkins checks out the latest source code.
2. Python dependencies are installed.
3. Existing tests are executed.
4. Any existing process using port `5001` is stopped.
5. `scripts/deploy.py` starts the application.
6. Waitress serves the Flask application on port `5001`.
7. Jenkins runs the health-check script.
8. The deployment is considered successful only when the health check passes.

## Deployment Result

The application was successfully started on:

`http://127.0.0.1:5001`

The application responded successfully to the health endpoint.

## Week 8 Outcome

Automated server deployment was successfully integrated into the Jenkins pipeline.