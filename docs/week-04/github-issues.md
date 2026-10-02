# GitHub Issues and Backlog

To manage the work for the upcoming weeks, the following GitHub Issues represent the approved Week 2 backlog. These should be tracked using GitHub Issues or a GitHub Project Board.

## Feature Implementation (Weeks 5-6)

### Issue #1: Implement Article Submission
*   **Description:** Create the frontend form and backend POST API to allow a Writer to submit a new news article.
*   **Labels:** `feature`, `priority-high`
*   **Acceptance Criteria:** Article is saved to the SQLite database with status 'SUBMITTED'.

### Issue #2: Implement Article Validation
*   **Description:** Ensure that required fields (title, content, author) are validated on the backend.
*   **Labels:** `feature`, `priority-high`
*   **Acceptance Criteria:** API returns 400 Bad Request with error message if fields are missing.

### Issue #3: Implement Reviewer Dashboard
*   **Description:** Create the frontend view and backend GET API to list all submitted articles.
*   **Labels:** `feature`, `priority-high`
*   **Acceptance Criteria:** Reviewer can see a list of articles and their statuses.

### Issue #4: Implement Article Approval
*   **Description:** Create the API endpoint and UI button to approve an article.
*   **Labels:** `feature`, `priority-medium`
*   **Acceptance Criteria:** Status changes to 'APPROVED' in the database.

### Issue #5: Implement Article Rejection
*   **Description:** Create the API endpoint and UI prompt to reject an article with a mandatory comment.
*   **Labels:** `feature`, `priority-medium`
*   **Acceptance Criteria:** Status changes to 'REJECTED' and comment is saved. Backend blocks rejection without a comment.

### Issue #6: Implement Status Tracking
*   **Description:** Ensure article status is visible in the dashboard and detail views.
*   **Labels:** `feature`, `priority-medium`
*   **Acceptance Criteria:** Users can easily identify if an article is SUBMITTED, APPROVED, or REJECTED.

## Testing & CI/CD Pipeline (Weeks 7-15)

### Issue #7: Develop Unit Tests
*   **Description:** Write pytest unit tests for backend logic and API endpoints.
*   **Labels:** `testing`, `priority-high`
*   **Relevant Week:** Week 5-6

### Issue #8: Develop Selenium Tests
*   **Description:** Write automated UI tests using Selenium WebDriver.
*   **Labels:** `testing`, `priority-medium`
*   **Relevant Week:** Week 9

### Issue #9: Configure Jenkins CI
*   **Description:** Set up Jenkins and configure a pipeline to build the app and run unit tests on every commit.
*   **Labels:** `ci`, `devops`, `priority-high`
*   **Relevant Week:** Week 7-8

### Issue #10: Containerize Application with Docker
*   **Description:** Create a Dockerfile to package the Flask app, Gunicorn, and dependencies.
*   **Labels:** `docker`, `devops`, `priority-high`
*   **Relevant Week:** Week 11

### Issue #11: Configure Jenkins Docker CD
*   **Description:** Update Jenkins pipeline to build the Docker image and deploy it.
*   **Labels:** `cd`, `devops`, `docker`, `priority-high`
*   **Relevant Week:** Week 12

### Issue #12: Automate Provisioning with Ansible
*   **Description:** Write Ansible playbooks to provision the target environment and deploy the Docker container.
*   **Labels:** `ansible`, `devops`, `priority-medium`
*   **Relevant Week:** Week 13

### Issue #13: Implement Health Check/Recovery
*   **Description:** Add pipeline steps to verify application health post-deployment.
*   **Labels:** `ci`, `devops`, `priority-medium`
*   **Relevant Week:** Week 14

### Issue #14: Final End-to-End Release
*   **Description:** Complete documentation and final test of the full pipeline from commit to deployment.
*   **Labels:** `documentation`, `devops`, `priority-high`
*   **Relevant Week:** Week 15

## Issue Labels
The following labels will be used in the repository:
*   `feature`, `bug`, `documentation`, `testing`, `devops`, `ci`, `cd`, `docker`, `ansible`
*   `priority-high`, `priority-medium`, `priority-low`
