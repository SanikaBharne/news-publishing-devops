# Week 10 - Pipeline Stages

The root `Jenkinsfile` now executes these stages in order:

1. **Checkout** - retrieves the configured source revision.
2. **Install Dependencies** - creates `venv` and installs `requirements.txt`.
3. **Run Unit Tests** - runs the two unit-test modules and verifies 14 tests.
4. **Deploy Application** - stops a prior listener on port 5001 and starts `scripts\deploy.py` in the background.
5. **Health Check** - verifies the `/health` endpoint before browser testing.
6. **Run Selenium Tests** - runs the existing Selenium suite with verbose output.
7. **Final Verification** - checks the application health endpoint again.

The `post` block always stops the listener on port 5001 and reports pipeline success or failure.
