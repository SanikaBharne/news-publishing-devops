# CI/CD Pipeline for a News Publishing Workflow

## 1. Project Description
This is a 15-week academic DevOps project. The goal is to build a small, simple News Publishing Workflow application and progressively apply Git/GitHub, Jenkins CI, automated Selenium testing, Docker, Jenkins-based continuous deployment, and Ansible/Puppet configuration management.

The primary academic objective is to demonstrate the progressive implementation of DevOps practices rather than to develop a full-scale news portal.

## 2. Problem Statement
Manual news publishing workflows lack automated testing, continuous integration, and standardized configuration management. Deployments are slow, error-prone, and inconsistent across environments. This project solves that by implementing an automated CI/CD pipeline.

## 3. MVP Scope
The Flask/SQLite MVP supports a public approved-story edition, Reader accounts and saved stories, and Publisher accounts for drafting, submission, and editorial review. Existing article statuses remain `DRAFT`, `SUBMITTED`, `APPROVED`, and `REJECTED`; the public edition exposes approved stories only. The workflow intentionally stops at editorial approval and does not implement publishing.

## 4. Key Features
**Currently Implemented:**
- Reader and Publisher session sign-in with hashed passwords, role checks, and CSRF protection.
- Public approved-story search, category filter, detail pages, and Reader bookmarks.
- Publisher drafts, submission, preview, dashboard, and review/approval/rejection workflow.
- Existing Flask JSON article APIs, SQLite persistence, and `/health` endpoint.
- pytest/Selenium tests, Docker packaging, and Jenkins pipeline.

## 5. Technology Stack
| Category | Selection | Status |
|---|---|---|
| Language | Python 3 | ✅ Installed |
| Frontend | HTML/CSS/JS + Jinja2 | ✅ Implemented |
| Backend | Flask | ✅ Installed |
| Database | SQLite | ✅ Implemented |
| Testing | pytest + Selenium | ✅ Implemented and locally verified |
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
- 6 pytest unit tests (all passing)
- Git workflow: `feature/article-submission` → `development`
- [Week 5 documentation](docs/week-05/week-05-summary.md)

## Week 6 – Reviewer Workflow, Approval/Rejection & MVP Completion

Status: Completed

- Created Reviewer Dashboard UI at `/reviewer` displaying submitted articles
- Implemented `PUT /api/articles/<id>/approve` endpoint (transitions status to `APPROVED`)
- Implemented `PUT /api/articles/<id>/reject` endpoint with mandatory rejection comment validation
- Exposed article details and status via `GET /api/articles/<id>`
- Added 8 unit tests in `tests/test_reviewer.py` (total 14/14 tests passing)
- Git workflow: `feature/reviewer-workflow` → `development`
- [Week 6 documentation](docs/week-06/week-06-summary.md)

## Week 7 – Jenkins Continuous Integration

Status: Completed

- Installed and configured Jenkins server
- Created declarative `Jenkinsfile` pipeline
- Configured Jenkins job to pull from GitHub `development` branch
- Automated Python virtual environment creation and dependency installation
- Automated `pytest` execution verifying 14/14 tests pass
- [Week 7 documentation](docs/week-07/week-07-summary.md)

## Week 11 – Docker Image and Container Lifecycle

Status: Completed

- Dockerfile, container lifecycle, health check, and SQLite volume instructions: [Week 11 documentation](docs/week-11/week-11-summary.md)
- Named-volume deployment and health-check records are available in the [Week 12 documentation](docs/week-12/week-12-summary.md).

## Weeks 12–14 – Deployment, Monitoring, and Readiness

- [Week 12: Jenkins and Docker deployment](docs/week-12/week-12-summary.md) — historical pipeline and deployment results.
- [Week 13: Deployment monitoring](docs/week-13/week-13-summary.md) — application, container, health, and evidence checks.
- [Week 14: Release readiness](docs/week-14/release-readiness.md) — original validation snapshot and the current integration update.
- [Current integration evidence](docs/evidence/week-14/current-redesign-verification.md) — latest local tests, deployed image identity, and authenticated Jenkins build/source verification.
- [Reader and Publisher setup and workflow](docs/newsflow-accounts.md).
- [NewsFlow UI and security notes](docs/newsflow-ui-redesign.md).

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
- **Week 8:** Advanced CI configurations ⏳
- **Week 9-10:** Selenium Tests and Continuous Testing ✅ (9 UI tests passed locally; redesign branch Jenkins run pending)
- **Week 11:** Docker Image and Container Lifecycle ✅
- **Week 12:** Jenkins-Docker Continuous Deployment ✅ (the latest verified Jenkins build used the Week 12 CD branch)
- **Week 13:** Deployment monitoring and evidence documentation ✅
- **Week 14:** Release-readiness documentation and NewsFlow integration on `feature/newsflow-ui-redesign` ✅; development merge, redesign Jenkins run, and screenshots remain pending
- **Week 15:** Final End-to-End Release and Documentation ⏳

## 12. Documentation Links
- [Week 1: Problem Definition & Scope](docs/week-01/week-01-summary.md)
- [Week 2: Agile Planning & DevOps Workflow](docs/week-02/week-02-summary.md)
- [Week 3: Requirements, Architecture & Tech Stack](docs/week-03/week-03-summary.md)
- [Week 4: Git/GitHub Setup & Branching Strategy](docs/week-04/branching-strategy.md)
- [Week 5: Article Submission Feature](docs/week-05/week-05-summary.md)
- [Week 6: Reviewer Workflow & MVP Completion](docs/week-06/week-06-summary.md)
- [Week 7: Jenkins CI Pipeline](docs/week-07/week-07-summary.md)
- [Week 12: Jenkins-Docker deployment](docs/week-12/week-12-summary.md)
- [Week 13: Deployment monitoring](docs/week-13/week-13-summary.md)
- [Week 14: Release readiness](docs/week-14/release-readiness.md)
- [Week 14 evidence checklist](docs/week-14/evidence-checklist.md)
- [NewsFlow Reader/Publisher account setup](docs/newsflow-accounts.md)
- [NewsFlow redesign and verification](docs/newsflow-ui-redesign.md)
- [Evidence Checklists](docs/evidence/)

## 13. Future DevOps Components
Ansible/Puppet provisioning remains outside the implemented project scope. Jenkins, Docker packaging/deployment, Selenium testing, and the Gunicorn-based Docker runtime are already present; see the linked Week 12–14 records for the limits and verification status.
