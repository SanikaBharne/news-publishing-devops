# Week 3 Summary: Requirements, Architecture and Technology Setup

## Week 3 Objective
Convert the approved Week 1 scope and Week 2 Agile plan into concrete requirements, architecture, technology selections, and a working local development environment.

## Work Completed
- SRS summary with 10 functional and 10 non-functional requirements.
- 5 use cases documented with full flows and a use-case diagram.
- 3 architecture diagrams: Application, DevOps/CI-CD, and Deployment.
- Technology stack finalized and documented with rationale.
- Data model designed (single `articles` table, 7 fields).
- API specification created (6 endpoints including health check).
- Project folder structure documented.
- Local development environment set up and verified.

## Technology Stack
| Category | Selection | Version |
|---|---|---|
| Language | Python | 3.14.7 |
| Frontend | HTML/CSS/JS + Jinja2 | 3.1.6 |
| Backend | Flask | 3.1.3 |
| Database | SQLite | Bundled with Python |
| Testing | pytest | 9.1.1 |
| VCS | Git | 2.52.0 |

## Architecture Completed
- **Application:** Browser → Flask (Jinja2 + REST API) → SQLite.
- **DevOps:** Developer → Git/GitHub → Jenkins → Build → Test → Quality Gate → Docker → Ansible → Container Deployment → Health Check.
- **Deployment:** Flask + Gunicorn inside a Docker container on a server provisioned by Ansible.

## Data Model Completed
Single `articles` table: id, title, content, author, status, comment, submission_date.

## API Design Completed
6 endpoints: health, submit article, list articles, article details, approve, reject.

## Local Setup
- Flask installed and running.
- `/health` endpoint verified returning `{"status":"ok"}`.
- pytest installed and available.

## Verification Results
All 8 verification checks passed. Database verification deferred (SQLite not yet created).

## Problems Encountered
- pip PATH warnings on Windows (scripts directory not on PATH). This does not affect functionality.

## Solutions
- Tools can be invoked directly or via `python -m` prefix if needed.

## What Is NOT Implemented Yet
- No application features (submission, review, approval, rejection).
- No Jinja2 templates or static files.
- No SQLite database file.
- No Jenkins, Dockerfile, Selenium tests, or Ansible playbooks.

## Pending Work (Future Weeks)
- Week 4: Git and GitHub repository initialization.
- Week 5-6: Feature development (implementing the MVP).
- Week 7+: DevOps pipeline implementation.

## Week 4 Preparation
The local development environment is verified and ready. The next step is to initialize the Git repository and push the project to GitHub.
