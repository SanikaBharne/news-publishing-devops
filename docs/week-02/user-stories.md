# User Stories

## Writer Stories
- **US-01:** As a Writer, I want to submit a news article, so that it can be reviewed for publishing.
- **US-02:** As a Writer, I want to enter required article information (title, content, author), so that the submission is complete and identifiable.
- **US-03:** As a Writer, I want to receive validation feedback if my submission is incomplete, so that I can correct errors before submitting.
- **US-04:** As a Writer, I want to view the status of my submission, so that I know if it is pending, approved, or rejected.

## Reviewer Stories
- **US-05:** As a Reviewer, I want to view a dashboard of pending submitted articles, so that I can see what needs reviewing.
- **US-06:** As a Reviewer, I want to view the details of a submitted article, so that I can evaluate its content.
- **US-07:** As a Reviewer, I want to approve an article, so that its status updates to approved.
- **US-08:** As a Reviewer, I want to reject an article and provide a mandatory comment, so that the writer knows why it was rejected.
- **US-09:** As a Reviewer, I want the article status to update immediately after my action, so that the dashboard reflects the current state.

## Application / System Stories
- **SYS-01:** As a System, I want to ensure roles can be simulated (Writer/Reviewer), so that users can switch views without complex authentication.

## DevOps Stories
- **DEV-01:** As a DevOps Engineer, I want the application to build automatically upon code commit, so that integration issues are caught early.
- **DEV-02:** As a DevOps Engineer, I want automated UI tests to run on every build, so that core functionality is continuously verified.
- **DEV-03:** As a DevOps Engineer, I want deployment to be blocked when tests fail, so that broken code never reaches the target environment.
- **DEV-04:** As a DevOps Engineer, I want successful builds to be packaged using Docker, so that the application runs consistently anywhere.
- **DEV-05:** As a DevOps Engineer, I want to automatically provision and configure the deployment environment, so that infrastructure setup is reproducible and reliable.
