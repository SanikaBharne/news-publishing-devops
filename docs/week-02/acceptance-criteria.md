# Acceptance Criteria

| User Story ID | Acceptance Criteria |
|---|---|
| **US-01 & US-02** | **Given** a writer is on the submission page, **When** they fill in title, content, and author and click submit, **Then** the system should save the article with a "Pending" status and confirm submission. |
| **US-03** | **Given** a writer is submitting an article, **When** the title or content is empty, **Then** the system should reject the submission and display a validation error message. |
| **US-04** | **Given** a writer has submitted an article, **When** they view their submissions, **Then** they should see the current status (Pending, Approved, Rejected). |
| **US-05 & US-06** | **Given** a reviewer logs into the dashboard, **When** there are pending articles, **Then** they should see a list of articles and be able to click one to read the full content. |
| **US-07 & US-09** | **Given** a reviewer is viewing a pending article, **When** they click "Approve", **Then** the article status should change to "Approved" and it should be removed from the pending queue. |
| **US-08 & US-09** | **Given** a reviewer is rejecting an article, **When** they click "Reject" without a comment, **Then** the system blocks the rejection and prompts for a mandatory comment. **When** they provide a comment and reject, **Then** the status changes to "Rejected" with the comment attached. |
| **DEV-01** | **Given** code is pushed to the repository, **When** the push completes, **Then** the CI server should automatically trigger a build job. |
| **DEV-02 & DEV-03** | **Given** a build is triggered, **When** the automated tests fail, **Then** the build is marked as failed and the deployment stage is not executed. |
| **DEV-04** | **Given** a build is successful, **When** packaging begins, **Then** a Docker image is created successfully containing the compiled application. |
| **DEV-05** | **Given** an empty target environment, **When** the configuration management scripts run, **Then** the server is provisioned with all necessary dependencies to run the Docker container. |
