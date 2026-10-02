# Project Structure

## Actual Structure (as of Week 3)

The following shows the actual files and folders that currently exist in the repository.

```
DevopsProject/
├── README.md                          # Project overview, roadmap, and status
├── requirements.txt                   # Python dependencies (Flask, pytest)
│
├── src/                               # Application source code
│   └── app.py                         # Minimal Flask skeleton with /health endpoint
│
└── docs/                              # Project documentation
    ├── week-01/                        # Week 1: Problem Definition and Scope
    │   ├── problem-definition.md
    │   ├── stakeholders.md
    │   ├── objectives-and-success-criteria.md
    │   ├── mvp-scope.md
    │   └── week-01-summary.md
    │
    ├── week-02/                        # Week 2: Agile Planning and DevOps Workflow
    │   ├── user-stories.md
    │   ├── acceptance-criteria.md
    │   ├── product-backlog.md
    │   ├── agile-plan.md
    │   ├── task-board.md
    │   ├── definition-of-done.md
    │   ├── devops-lifecycle.md
    │   ├── devops-workflow.md
    │   ├── dependencies-and-risks.md
    │   └── week-02-summary.md
    │
    ├── week-03/                        # Week 3: Requirements, Architecture, Technology
    │   └── (19 documentation files)
    │
    └── evidence/                       # Evidence checklists and screenshots
        ├── week-02/
        │   └── evidence-checklist.md
        └── week-03/
            └── evidence-checklist.md
```

## Planned Additions (Future Weeks)

The following folders and files are planned but do NOT exist yet:

| Folder/File | Purpose | Week |
|---|---|---|
| `src/templates/` | Jinja2 HTML templates | Week 5-6 |
| `src/static/` | CSS, JS, images | Week 5-6 |
| `tests/unit/` | pytest unit tests | Week 5-6 |
| `tests/selenium/` | Selenium UI test scripts | Week 9 |
| `Jenkinsfile` | Pipeline as Code | Week 8 |
| `Dockerfile` | Container definition | Week 11 |
| `ansible/` | Ansible playbooks | Week 13 |
