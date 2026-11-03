# NewsFlow – CI/CD Pipeline for a News Publishing Workflow

## 1. Project Description
NewsFlow is a 15-week academic DevOps project: a Flask/SQLite article-submission and editorial-review workflow used to demonstrate Git/GitHub, Jenkins CI, Selenium testing, and Docker deployment practices. The application stops at editorial approval; it does not implement a separate article-publishing action. Ansible/Puppet configuration management is outside the implemented scope.

The primary academic objective is to demonstrate the progressive implementation of DevOps practices rather than to develop a full-scale news portal.

## 2. Problem Statement
Manual editorial workflows and software deployments can lack repeatable testing and consistent release practices. NewsFlow demonstrates an article-review workflow alongside automated testing and documented CI/CD and deployment components.

## 3. MVP Scope
The Flask/SQLite MVP supports a public approved-story edition, Reader accounts and saved stories, and Publisher accounts for drafting, submission, and editorial review. Existing article statuses remain `DRAFT`, `SUBMITTED`, `APPROVED`, and `REJECTED`; the public edition exposes approved stories only. The workflow intentionally stops at editorial approval and does not implement publishing.

## 4. Key Features
**Currently Implemented:**
- Reader and Publisher session sign-in with hashed passwords, role checks, and CSRF protection.
- Public approved-story search, category filter, detail pages, and Reader bookmarks.
- Publisher drafts, submission, preview, dashboard, and review/approval/rejection workflow.
- Existing Flask JSON article APIs, SQLite persistence, and `/health` endpoint.
- pytest/Selenium tests, Docker packaging, and a Jenkins pipeline. Jenkins build #4 verified Maven-based Python syntax validation, tests, Docker staging deployment, and health checks for commit `928aebe`.

## 5. Technology Stack
| Category | Selection | Status |
|---|---|---|
| Language | Python 3 | ✅ Installed |
| Frontend | HTML/CSS/JS + Jinja2 | ✅ Implemented |
| Backend | Flask | ✅ Installed |
| Database | SQLite | ✅ Implemented |
| Testing | pytest + Selenium | ✅ Locally verified: 24 backend and 9 Selenium tests passed |
| Version Control | Git + GitHub | ✅ Initialized |

## 6. Project Structure
```
project-root/
├── src/                         # Application source code
│   └── app.py
├── tests/                       # pytest and Selenium tests
├── docs/                        # Project documentation
│   ├── week-01/
│   ├── week-02/
│   ├── week-03/
│   ├── week-04/
│   └── evidence/
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview
```

## 7. Current Project Status

**Latest release verification (2026-11-03):** Jenkins job `NewsFlow-Week15-Final`, build #4 on commit `928aebe`, succeeded. Maven validation passed; 24 backend tests and 9 Selenium tests passed; the Docker image deployed to isolated staging and passed health checks at `http://127.0.0.1:5016`. The Jenkins console log is in [Week 15 evidence](docs/evidence/week-15/jenkins-build-4-console.txt). Persistence after restarting this exact release container, screenshots, and final PR/merge remain pending.

## Week 4 – Git/GitHub Initialization

Status: Completed

- Git repository setup
- GitHub repository
- repository structure
- .gitignore
- branching strategy
- commit convention
- GitHub issues
- Pull Request workflow
- [Week 4 documentation links](docs/week-04/week-04-summary.md)

## Week 5 – Article Submission with Required-Field Validation

Status: Completed

- Implemented `POST /api/articles` endpoint with server-side validation
- Created HTML frontend submission form
- Required-field validation (title, content, author)
- Whitespace-only rejection via `.strip()`
- SQLite persistence with status `SUBMITTED`
- 6 pytest unit tests passed at the Week 5 milestone (historical count; current backend suite: 24 passed)
- Git workflow: `feature/article-submission` → `development`
- [Week 5 documentation](docs/week-05/week-05-summary.md)

## Week 6 – Reviewer Workflow, Approval/Rejection & MVP Completion

Status: Completed

- Created Reviewer Dashboard UI at `/reviewer` displaying submitted articles
- Implemented `PUT /api/articles/<id>/approve` endpoint (transitions status to `APPROVED`)
- Implemented `PUT /api/articles/<id>/reject` endpoint with mandatory rejection comment validation
- Exposed article details and status via `GET /api/articles/<id>`
- Added 8 unit tests in `tests/test_reviewer.py` (14 tests passed at the Week 6 milestone; current backend suite: 24 passed)
- Git workflow: `feature/reviewer-workflow` → `development`
- [Week 6 documentation](docs/week-06/week-06-summary.md)

## Week 7 – Jenkins Continuous Integration

Status: Completed

- Jenkins server and declarative pipeline were configured; the Week 15 Maven-enabled pipeline passed in build #4
- Created declarative `Jenkinsfile` pipeline
- Configured Jenkins job to pull from GitHub `development` branch
- Automated Python virtual environment creation and dependency installation
- Maven validates Python syntax from `pom.xml` before pytest; Maven does not compile the Flask application
- [Week 7 documentation](docs/week-07/week-07-summary.md)

## Weeks 8–10 – Deployment Checks and Selenium Testing

- **Week 8:** Deployment scripts and health checks ran successfully in Jenkins build #4 against isolated staging. [Week 8 summary](docs/week-08/week-08-summary.md)
- **Week 9:** Selenium end-to-end tests are implemented; all 9 passed in the current local audit. [Week 9 summary](docs/week-09/week-09-summary.md)
- **Week 10:** Jenkins build #4 ran all 9 Selenium tests against the fixture's isolated temporary server; deployment was checked separately by the health-check stage. Selenium was not pointed at the deployed container. [Week 10 summary](docs/week-10/week-10-summary.md)

## Week 11 – Docker Image and Container Lifecycle

Status: Docker image build, isolated container deployment, and health check passed in Jenkins build #4. The running staging container uses port 5016 and volume `newsflow-week15-staging-data`.

- Dockerfile, container lifecycle, health check, and SQLite volume instructions: [Week 11 documentation](docs/week-11/week-11-summary.md)
- Current pipeline/deployment evidence is in [Week 15 build logs](docs/evidence/week-15/jenkins-build-4-console.txt); persistence after restarting this exact release container remains unverified.

## Weeks 12–15 – Deployment, Monitoring, and Final Validation

- [Week 12: Jenkins and Docker deployment](docs/week-12/week-12-summary.md) — historical integration records; current deployment verification is recorded under Week 15.
- [Week 13: Deployment monitoring](docs/week-13/week-13-summary.md) — historical application, container, health, and evidence checks.
- [Week 14: Release readiness](docs/week-14/release-readiness.md) — dated validation records, not current-release verification.
- [Week 14 integration evidence](docs/evidence/week-14/current-redesign-verification.md) — records historical tests, deployment, and Jenkins evidence for earlier source revisions.
- [Reader and Publisher setup and workflow](docs/newsflow-accounts.md).
- [NewsFlow UI and security notes](docs/newsflow-ui-redesign.md).
- **Week 15:** Maven validation, 24 backend tests, 9 Selenium tests, Docker staging, and health checks passed in Jenkins build #4. Restart persistence for this release, final PR/merge, and screenshots remain pending. [Week 15 summary](docs/week-15/week-15-summary.md)

## 8. How to Run Locally
1. Ensure Python 3.x is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure private demo credentials and start the Windows-compatible deployment:
   ```bash
   $env:DEMO_READER_USERNAME = "reader-demo"
   $securePassword = Read-Host "Reader password" -AsSecureString
   $env:DEMO_READER_PASSWORD = [System.Net.NetworkCredential]::new("", $securePassword).Password
   $env:DEMO_PUBLISHER_USERNAME = "publisher-demo"
   $securePassword = Read-Host "Publisher password" -AsSecureString
   $env:DEMO_PUBLISHER_PASSWORD = [System.Net.NetworkCredential]::new("", $securePassword).Password
   python scripts/deploy.py
   ```
   Account setup, reviewer account, Docker volume commands, and secret handling are documented in [NewsFlow account setup](docs/newsflow-accounts.md).
4. Verify the health endpoint at `http://127.0.0.1:5001/health`.

## 9. How to Run Tests
Run the pytest test suite:
```bash
python -m pytest -v
```
Latest local audit: **24 backend tests passed, 9 Selenium tests passed (33 total)**. Jenkins build #4 also passed the Maven validation, both test suites, Docker deployment, and health checks. Persistence after restarting this exact release container has not been checked.

## 10. Git Branching Strategy
We follow a structured branching model:
- `main`: Stable, release-ready branch.
- `development`: Main integration branch.
- `feature/*`: Individual feature branches (e.g., `feature/article-submission`).
Features are merged into `development` via Pull Requests.

## 11. 15-Week Roadmap
- **Week 1-3:** Problem Definition, Agile Planning, Architecture Setup ✅
- **Week 4:** Git and GitHub Repository Initialization ✅
- **Week 5:** Article Submission with Validation ✅
- **Week 6:** MVP Completion (Dashboard, Approval, Rejection, Status Tracking) ✅
- **Week 7:** Jenkins CI and Pipeline as Code ✅
- **Week 8:** Deployment scripts and health checks verified in Jenkins build #4 ✅
- **Week 9:** Selenium end-to-end testing ✅ (9 tests passed locally)
- **Week 10:** Jenkins ran the isolated Selenium suite (9 passed); a separate health check verified staging ✅
- **Week 11:** Docker image build, isolated staging deployment, and health check verified in Jenkins build #4 ✅
- **Week 12:** Jenkins-Docker pipeline and staging deployment verified; restart persistence for this release remains pending ⏳
- **Week 13:** Deployment monitoring and evidence documentation ✅
- **Week 14:** Release-readiness documentation and NewsFlow integration on `feature/newsflow-ui-redesign` ✅; development merge, redesign Jenkins run, and screenshots remain pending
- **Week 15:** Maven-enabled Jenkins build #4 passed (24 backend + 9 Selenium; 33 total), Docker staging, and health checks; current-release restart persistence, screenshots, and final PR/merge remain pending ⏳

## 12. Documentation Links
- [Week 1: Problem Definition & Scope](docs/week-01/week-01-summary.md)
- [Week 2: Agile Planning & DevOps Workflow](docs/week-02/week-02-summary.md)
- [Week 3: Requirements, Architecture & Tech Stack](docs/week-03/week-03-summary.md)
- [Week 4: Git/GitHub Setup & Branching Strategy](docs/week-04/branching-strategy.md)
- [Week 5: Article Submission Feature](docs/week-05/week-05-summary.md)
- [Week 6: Reviewer Workflow & MVP Completion](docs/week-06/week-06-summary.md)
- [Week 7: Jenkins CI Pipeline](docs/week-07/week-07-summary.md)
- [Week 8: Deployment and health validation](docs/week-08/week-08-summary.md)
- [Week 9: Selenium end-to-end testing](docs/week-09/week-09-summary.md)
- [Week 10: Jenkins-Selenium integration](docs/week-10/week-10-summary.md)
- [Week 11: Docker image and container lifecycle](docs/week-11/week-11-summary.md)
- [Week 12: Jenkins-Docker deployment](docs/week-12/week-12-summary.md)
- [Week 13: Deployment monitoring](docs/week-13/week-13-summary.md)
- [Week 14: Release readiness](docs/week-14/release-readiness.md)
- [Week 14 evidence checklist](docs/week-14/evidence-checklist.md)
- [NewsFlow Reader/Publisher account setup](docs/newsflow-accounts.md)
- [NewsFlow redesign and verification](docs/newsflow-ui-redesign.md)
- [NewsFlow DevOps white paper (six-page A4 HTML)](docs/white-paper/newsflow-devops-white-paper.html)
- [Evidence Checklists](docs/evidence/)

## 13. Future DevOps Components
Ansible/Puppet provisioning remains outside the implemented project scope. The Maven-enabled Jenkins pipeline, Docker staging deployment, Selenium testing, and Gunicorn-based Docker runtime were verified in build #4; database restart persistence for this exact release, screenshots, and final PR/merge remain outstanding. See the linked Week 12–15 records for evidence and remaining limits.
