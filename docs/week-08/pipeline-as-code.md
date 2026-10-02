# Week 8 – Pipeline as Code

## Objective

The objective of Week 8 was to extend the Jenkins Continuous Integration pipeline by adding automated application deployment and health checking.

The Jenkins pipeline was maintained as code using a root-level `Jenkinsfile`. This makes the CI/CD workflow version-controlled, repeatable, and easier to maintain.

## Jenkins Pipeline Stages

The Jenkinsfile contains the following stages:

1. **Checkout**

   * Retrieves the project source code from the configured Git repository.

2. **Install Dependencies**

   * Installs the Python dependencies listed in `requirements.txt`.

3. **Run Tests**

   * Executes the existing pytest test suite.

4. **Deploy Application**

   * Starts the Flask application using a Windows-compatible WSGI server.
   * The application is deployed on port `5001`.

5. **Health Check**

   * Checks the `/health` endpoint.
   * The pipeline performs multiple attempts and fails if the application does not become healthy.

## Benefits

Pipeline as Code provides:

* Version-controlled pipeline configuration
* Repeatable deployment steps
* Automated testing before deployment
* Automated health verification
* Easier maintenance of the DevOps workflow

## Week 8 Outcome

The Jenkins pipeline was successfully extended from basic CI to include application deployment and automated health checking.