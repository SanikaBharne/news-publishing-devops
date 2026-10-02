# CI/CD Pipeline for a News Publishing Workflow

## 1. Project Description
This is a 15-week academic DevOps project. The goal is to build a small, simple News Publishing Workflow application and progressively apply Git/GitHub, Jenkins CI, automated Selenium testing, Docker, Jenkins-based continuous deployment, and Ansible/Puppet configuration management.

The primary academic objective is to demonstrate the progressive implementation of DevOps practices rather than to develop a full-scale news portal.

## 2. Problem Statement
Manual news publishing workflows lack automated testing, continuous integration, and standardized configuration management. Deployments are slow, error-prone, and inconsistent across environments. This project solves that by implementing an automated CI/CD pipeline.

## 3. MVP Scope
The application MVP contains ONLY:
- News article/request submission
- Required-field/data validation
- Reviewer dashboard
- Reviewer approval
- Reviewer rejection with mandatory rejection comment
- Article status tracking

*(Note: The application is monolithic. Authentication, RBAC, microservices, and other complex features are explicitly out of scope).*

## 4. Key Features
**Currently Implemented:**
- Minimal Flask application skeleton with a `/health` endpoint.
- Local development environment configured.
- Git repository initialized.

**Planned for Future Weeks:**
- Article submission form and validation logic.
- Reviewer dashboard with approve/reject actions.
- Status tracking visibility.
- Automated CI/CD pipelines and deployment.

## 5. Technology Stack
| Category | Selection | Status |
|---|---|---|
| Language | Python 3 | ✅ Installed |
| Frontend | HTML/CSS/JS + Jinja2 | ⏳ Planned |
| Backend | Flask | ✅ Installed |
| Database | SQLite | ⏳ Planned |
| Testing | pytest + Selenium (Week 9) | ✅ pytest Installed |
| Version Control | Git + GitHub | ✅ Initialized |

## 6. Project Structure
```
project-root/
├── src/                         # Application source code
│   └── app.py
├── tests/                       # Automated tests (Planned)
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
**Week 4 - Git/GitHub Initialization and Repository Setup** is currently completed.
- Git repository initialized.
- Branching strategy and commit convention defined.
- Project structure established.

## 8. How to Run Locally
1. Ensure Python 3.x is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python src/app.py
   ```
4. Verify the health endpoint at `http://127.0.0.1:5000/health`.

## 9. How to Run Tests
*(Planned for Future Weeks)*
Once tests are implemented in Week 5-6, run them using:
```bash
pytest
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
- **Week 5-6:** Feature Development and MVP Completion ⏳
- **Week 7-8:** Jenkins CI and Pipeline as Code ⏳
- **Week 9-10:** Selenium Tests and Continuous Testing ⏳
- **Week 11:** Docker Image and Container Lifecycle ⏳
- **Week 12:** Jenkins-Docker Continuous Deployment ⏳
- **Week 13-14:** Ansible Configuration and Automated Provisioning ⏳
- **Week 15:** Final End-to-End Release and Documentation ⏳

## 12. Documentation Links
- [Week 1: Problem Definition & Scope](docs/week-01/week-01-summary.md)
- [Week 2: Agile Planning & DevOps Workflow](docs/week-02/week-02-summary.md)
- [Week 3: Requirements, Architecture & Tech Stack](docs/week-03/week-03-summary.md)
- [Week 4: Git/GitHub Setup & Branching Strategy](docs/week-04/branching-strategy.md)
- [Evidence Checklists](docs/evidence/)

## 13. Future DevOps Components
The following are **NOT** currently implemented, but are planned for future weeks:
- Jenkins server for Continuous Integration.
- Docker containers for packaging the application.
- Selenium WebDriver for UI automation testing.
- Ansible playbooks for environment provisioning.
- Gunicorn server for production deployment.
