# Week 8 – Jenkinsfile Implementation

## Objective

The Jenkinsfile was updated to support automated deployment and post-deployment health verification.

## Pipeline Stages

The updated Jenkinsfile contains five stages:

### 1. Checkout

```text
checkout scm
```

This retrieves the source code from the configured repository.

### 2. Install Dependencies

```text
pip install -r requirements.txt
```

This installs all required Python packages.

### 3. Run Tests

```text
python -m pytest -v
```

The existing automated test suite is executed before deployment.

### 4. Deploy Application

The deployment stage starts:

```text
scripts/deploy.py
```

The application runs on port:

```text
5001
```

Waitress is used as the WSGI server for the Windows environment.

### 5. Health Check

The Jenkins pipeline executes:

```text
scripts/healthcheck.py
```

The script checks the `/health` endpoint and retries if the application has not started yet.

## Failure Handling

The pipeline is configured so that a failed health check causes the deployment pipeline to fail.

## Result

The Jenkinsfile now represents a basic CI/CD workflow:

```text
Checkout
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Deploy Application
   ↓
Health Check
```

This establishes the foundation for the more advanced deployment automation introduced in later weeks.