# NewsFlow – Week 15 Final Validation Summary

## Project: NewsFlow DevOps

This is a consolidated summary of the 15-week academic **NewsFlow – CI/CD Pipeline for a News Publishing Workflow** project, prepared for mentor review. The Flask/SQLite application supports article submission, editorial review, and reader access to approved stories; it stops at editorial approval and does not implement a separate publishing action. Ansible/Puppet configuration management is outside the implemented scope.

---

## Week 1 – Problem Definition and Scope

The project began with identifying the problem of manual deployment and inconsistent release workflows. The main users were news writers and reviewers/editors. The objective was to build a simple but functional news publishing workflow and to implement DevOps practices such as automation, testing, deployment, and release readiness. The project scope was limited to a monolithic application with no unnecessary features, and the success criteria focused on article submission, review, approval, and status tracking.

## Week 2 – Agile Planning and DevOps Work

Week 2 translated the problem statement into an Agile roadmap. The team created user stories, acceptance criteria, a product backlog, a 15-week plan, and a Kanban-style task board. The DevOps lifecycle was mapped from planning and coding to build, test, release, deploy, operate, and monitor. Key risks and dependencies were identified, and a Definition of Done was established so that work was only considered complete after validation and Git readiness.

## Week 3 – Requirements, Architecture, and Technology Setup

This week converted the project problem into a concrete technical design. The architecture, technology stack, use cases, requirements, data model, and API specification were documented. The selected stack included Python, Flask, SQLite, pytest, Git, and supporting deployment tools. The application architecture was defined as a browser-to-Flask-to-SQLite flow, while the DevOps architecture included GitHub, Jenkins, Docker, and deployment automation. The local environment was also configured and verified.

## Week 4 – Git and GitHub Setup

Week 4 focused on version control best practices. The repository structure was organized into source, tests, docs, and configuration files. A `.gitignore`, README, standard branching approach, and commit conventions were established. The project followed a branching strategy with `main`, `development`, and `feature/*` branches, and a sample pull request workflow was demonstrated. This created a clean foundation for development and team-based collaboration.

## Week 5 – Article Submission and Validation

The first MVP feature implemented was article submission. The Flask API accepted article details and stored valid submissions in SQLite with the status `SUBMITTED`. Required-field validation was added so missing or whitespace-only fields were rejected with a clear error response. Automated tests were written to verify valid and invalid cases, and the feature was merged into the development branch after successful validation.

## Week 6 – Reviewer Workflow and Status Tracking

Week 6 completed the core application MVP by adding the reviewer dashboard, article approval, article rejection, and status tracking. Reviewers could view submitted articles, approve them, or reject them with a mandatory comment. The app updated the article state accordingly and enforced validation rules for rejection comments. Automated tests confirmed the review workflow, and the feature was merged into the development branch.

## Week 7 – Jenkins CI Pipeline

The project moved into CI/CD automation in Week 7. The declarative `Jenkinsfile` checks out the selected branch, installs Python dependencies, runs Maven-based Python syntax validation, and executes the tests. Jenkins build #4 of `NewsFlow-Week15-Final` passed on commit `928aebe` on 2026-11-03.

## Week 8 – Jenkins Deployment and Health Validation

Week 8 added deployment scripts and HTTP health checks to the pipeline workflow. Jenkins build #4 deployed the image to isolated staging on port 5016 and the deployment health check passed.

## Week 9 – Selenium End-to-End Testing

The project introduced Selenium-based testing for article submission, reviewer dashboard behavior, approval, rejection with a comment, and form validation. In the current local audit, all 9 Selenium tests passed using the project's virtual environment and an isolated test server and database.

## Week 10 – Jenkins with Selenium Integration

The Jenkinsfile includes a Selenium test stage alongside deployment and health-check stages. All 9 Selenium tests passed in Jenkins build #4 against the fixture's isolated temporary server. A separate health-check stage verified the deployed staging container; Selenium itself does not test that container.

## Week 11 – Docker Packaging and Container Lifecycle

The Dockerfile and deployment scripts define image packaging, runtime health checks, and a persistent SQLite data path. Jenkins build #4 built image `news-publishing-app:week15-staging-build-4`, deployed it as `newsflow-week15-staging`, and verified its health. It used the isolated volume `newsflow-week15-staging-data`; restart persistence for this exact release container was not tested.

## Week 12 – Jenkins and Docker Deployment Integration

Week 12 documents Jenkins-Docker integration, deployment checks, and named-volume use. Current Jenkins-Docker integration was verified in build #4, including Docker build, staging deployment, and health checks. Database persistence across a restart of this exact release container has not been verified.

## Week 13 – Monitoring and Deployment Verification

Week 13 records historical checks of an application endpoint, container, and logs, and documents monitoring procedures. Those records do not establish that the current release is running or healthy.

## Week 14 – Release Readiness and Final Pre-Release Checks

Week 14 documented release-readiness checks and noted that historical deployment and test results needed fresh confirmation. At the time of the initial Week 15 audit, Jenkins and Docker execution and a live application health check had not yet been verified; the later build #4 results are recorded below.

## Week 15 – Final Validation, Release Preparation, and Documentation

Week 15 audited the application, test suites, Jenkins pipeline, Docker configuration, database, and documentation. Local testing passed **24 backend tests** and **9 Selenium tests** (**33 passed total; 0 failed, 0 skipped**). Jenkins build #4 on commit `928aebe` also passed Maven validation, all 33 tests, Docker image build, isolated staging deployment, health checks, and final verification. The staging application returned HTTP 200 at `http://127.0.0.1:5016`; its container uses the dedicated `newsflow-week15-staging-data` volume. The existing SQLite database previously passed a read-only integrity check, but restart persistence for this exact release container remains unverified. The genuine Jenkins console log is saved at `docs/evidence/week-15/jenkins-build-4-console.txt`. Screenshots and final PR/merge remain pending.

---

## Final Project Outcome

The NewsFlow project implements an article-submission and editorial-review workflow with DevOps practices developed across the project. The application supports submission, validation, reviewer dashboard actions, approval/rejection, and status tracking. It stops at editorial approval and does not implement a separate publishing action. Automated tests verified application behavior and user journeys locally and in Jenkins; build #4 verified the pipeline and isolated Docker staging, while release-container restart persistence remains pending.

The project demonstrates a realistic DevOps learning path that covers:
- application features and validation
- Git and GitHub workflow
- CI automation with Jenkins
- deployment automation and health checks
- browser-based UI testing with Selenium
- Docker packaging and deployment concepts
- release-readiness documentation and final validation

The verified results are **24 backend tests passed, 9 Selenium tests passed, 33 passed total** locally and in Jenkins build #4. That build also verified Maven-based Python syntax validation, Docker staging deployment, and application health; it did not test restart persistence for the deployed release container.

## Final Status Summary

### Verified working features
- Article submission works correctly
- Required fields are enforced
- Reviewer dashboard displays submitted articles
- Reviews can approve or reject articles
- Rejections require a clear comment
- Article status updates are tracked correctly
- Backend tests: **24 passed**; Selenium tests: **9 passed**; **33 passed total**
- The existing SQLite database passed a read-only integrity check; restart persistence for the current release is not verified

### Pending or environment-limited items
- Database persistence across a restart of the exact Jenkins build #4 staging container
- Screenshot evidence collection
- Week 15 PR creation, review, and merge

### Overall conclusion

The application workflows passed locally and in Jenkins build #4: 24 backend tests and 9 Selenium tests passed, and the Maven validation, Docker image build, isolated staging deployment, and health checks succeeded. Restart persistence for that exact deployed release, the final PR/merge, and screenshot evidence remain pending, so the project is not yet fully verified for final release.
