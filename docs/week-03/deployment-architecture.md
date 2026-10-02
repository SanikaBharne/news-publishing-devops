# Deployment Architecture

## Current Local Setup (Week 3)

The application currently runs only in a local development environment.

```mermaid
flowchart TD
    Dev([Developer Machine]) --> Python[Python 3.14.7]
    Python --> Flask[Flask Dev Server\nhttp://127.0.0.1:5000]
    Flask --> DB[(SQLite File\nLocal Filesystem)]
```

| Component | Status | Details |
|---|---|---|
| Flask Dev Server | Running locally | `python src/app.py` starts on port 5000 |
| SQLite Database | Not yet created | Will be created during Week 5-6 feature development |
| Health Endpoint | Verified | `/health` returns `{"status":"ok"}` |

## Future CI/CD Deployment (Planned for Weeks 11-14)

The planned target deployment architecture is shown below. **This is NOT yet implemented.**

```mermaid
flowchart TD
    Internet([Network]) --> Host[Target Deployment Server]

    subgraph Host[Target Server - Provisioned by Ansible]
        subgraph Container[Docker Container]
            Gunicorn[Gunicorn WSGI Server]
            App[Flask Application]
            DB[(SQLite File)]

            Gunicorn --> App
            App --> DB
        end
    end

    Jenkins([Jenkins]) -.->|Health Check| Gunicorn
```

| Component | Planned Tool | Implementation Week |
|---|---|---|
| Container Runtime | Docker | Week 11 |
| WSGI Server | Gunicorn | Week 11 |
| Server Provisioning | Ansible | Week 13-14 |
| CD Pipeline | Jenkins | Week 12 |
| Health Check | Jenkins | Week 14 |

**Important:** The deployment architecture is a plan. No Docker containers, Ansible playbooks, or Jenkins pipelines have been created yet.
