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

The project moved into CI/CD automation in Week 7. Jenkins and a declarative `Jenkinsfile` were configured for checkout, dependency installation, and test execution. Historical documentation describes earlier pipeline activity; the current release was not run in Jenkins, so its pipeline status is unverified.

## Week 8 – Jenkins Deployment and Health Validation

Week 8 added deployment scripts and HTTP health checks to the pipeline workflow. These components and historical deployment checks are documented, but Jenkins and deployment execution for the current release remain unverified.

## Week 9 – Selenium End-to-End Testing

The project introduced Selenium-based testing for article submission, reviewer dashboard behavior, approval, rejection with a comment, and form validation. In the current local audit, all 9 Selenium tests passed using the project's virtual environment and an isolated test server and database.

## Week 10 – Jenkins with Selenium Integration

The Jenkinsfile includes a Selenium test stage alongside deployment and health-check stages. The current pipeline was not run. The Selenium fixture starts an isolated local server, so its successful local run does not demonstrate testing against a deployed container.

## Week 11 – Docker Packaging and Container Lifecycle

The Dockerfile and deployment scripts define image packaging, runtime health checks, and a persistent SQLite data path. Historical Docker build/deployment records exist, but the Docker engine was unavailable during the current audit, so no current-release image or container was verified.

## Week 12 – Jenkins and Docker Deployment Integration

Week 12 documents Jenkins-Docker integration, deployment checks, and named-volume use. These are historical results, not a verification of the current release. The current Jenkins pipeline and Docker deployment were not run, and database persistence across a current-release application or container restart has not been verified.

## Week 13 – Monitoring and Deployment Verification

Week 13 records historical checks of an application endpoint, container, and logs, and documents monitoring procedures. Those records do not establish that the current release is running or healthy.

## Week 14 – Release Readiness and Final Pre-Release Checks

Week 14 documented release-readiness checks and noted that historical deployment and test results needed fresh confirmation. The current audit likewise found that Jenkins and Docker release execution and a live application health check remain unverified.

## Week 15 – Final Validation, Release Preparation, and Documentation

Week 15 audited the application, test suites, Jenkins pipeline, Docker configuration, database, and documentation. The current local audit passed **24 backend tests** and **9 Selenium tests** (**33 passed total; 0 failed, 0 skipped**). SQLite integrity was checked read-only and returned `ok`; persistence after a current-release restart was not tested. Jenkins job/build details require authentication, the Docker engine was unavailable, and the application health endpoint was unreachable. Therefore current-release Jenkins/Docker execution and deployment health remain unverified. No screenshots were found, and the Week 15 branch has no final pull request or merge.

---

## Final Project Outcome

The NewsFlow project implements an article-submission and editorial-review workflow with DevOps practices developed across the project. The application supports submission, validation, reviewer dashboard actions, approval/rejection, and status tracking. It stops at editorial approval and does not implement a separate publishing action. Automated tests verified application behavior and user journeys locally; current-release infrastructure verification remains pending.

The project demonstrates a realistic DevOps learning path that covers:
- application features and validation
- Git and GitHub workflow
- CI automation with Jenkins
- deployment automation and health checks
- browser-based UI testing with Selenium
- Docker packaging and deployment concepts
- release-readiness documentation and final validation

The current local test results are **24 backend tests passed, 9 Selenium tests passed, 33 passed total**. These local results do not imply that the Jenkins pipeline or Docker deployment succeeded for the current release.

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
- Current-release Jenkins pipeline execution and stage results
- Current-release Docker image build and container deployment validation
- Live health-check verification on the actual deployed app
- Database persistence across a current-release application/container restart
- Screenshot evidence collection
- Week 15 PR creation, review, and merge

### Overall conclusion

The application workflows are validated by the current local test suites: 24 backend tests and 9 Selenium tests passed. Jenkins and Docker results in earlier weekly records are historical; current-release pipeline execution, image build, deployment health, and database restart persistence remain unverified. The final PR and genuine screenshot evidence also remain pending, so the project is not yet a fully verified release.
