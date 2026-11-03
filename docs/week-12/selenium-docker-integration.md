# Selenium and Docker Integration

The existing Selenium fixture now reads `APP_BASE_URL`; without that variable it retains the local-testing default `http://127.0.0.1:5001`.

Jenkins sets:

```text
APP_BASE_URL=http://127.0.0.1:5001
```

After Docker deployment and health verification, the existing suite runs:

```bat
python -m pytest tests\selenium -v
```

The pipeline no longer starts `scripts\deploy.py` and does not target a separate Waitress server. The Selenium browser therefore tests the Docker-published service at the configured URL. For local Selenium runs, start the application as before or set `APP_BASE_URL` to another intended test deployment.

**Expected result:** all eight existing end-to-end tests pass. Tests fail the Jenkins build on a bad deployment or browser interaction. The test count and result are reported only after a real run.
