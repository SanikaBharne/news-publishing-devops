# Week 10 - Jenkins Continuous Testing

## Objective

Integrate the existing Week 9 Selenium end-to-end suite into the Windows Jenkins pipeline. Every pipeline run now installs dependencies, runs the 14 unit tests, starts the Week 8 Waitress deployment, runs the 8 Selenium tests, and performs final health verification.

## Continuous Testing

Continuous testing runs automated checks as part of CI so a change is not considered successful only because it builds or starts. Jenkins stops on a failed unit test, failed health check, or failed Selenium test.

The application remains local to the Jenkins agent at `http://127.0.0.1:5001`.
