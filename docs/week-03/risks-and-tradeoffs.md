# Risks and Trade-Offs

## Technical Risks

| Risk | Impact | Likelihood | Mitigation |
|---|---|---|---|
| SQLite file locking under Docker | Medium | Low | Only one container instance will run at a time in this academic project. |
| Flask development server used in early weeks | Low | Certain | Expected behavior. Gunicorn will replace it for Docker deployment in Week 11+. |
| Selenium tests flaky on different browsers | Medium | Medium | Keep tests simple. Use explicit waits instead of hardcoded sleeps. |
| Port conflicts (Jenkins 8080, Flask 5000) | Medium | Medium | Document port assignments. Use non-default ports if conflicts arise. |

## Setup Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Python version incompatibility | Medium | Verified Python 3.14.7 works with Flask 3.1.3 and pytest 9.1.1. |
| pip PATH warnings on Windows | Low | Scripts directory not on PATH but tools work via `python -m` if needed. |

## Database Risks

| Risk | Impact | Mitigation |
|---|---|---|
| SQLite not suitable for concurrent access | Low | MVP is single-user; no concurrency issue. |
| Database file lost if not in Docker volume | Medium | Mount SQLite file as a Docker volume in Week 11. |

## Deployment Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Docker networking issues | High | Start with a simple Dockerfile. Test locally before Jenkins integration. |
| Ansible connectivity to target server | High | Test playbooks against a local VM or localhost first. |

## Testing Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Selenium browser driver version mismatch | Medium | Use webdriver-manager or pin exact driver version. |
| UI changes breaking Selenium selectors | Medium | Use stable element IDs in HTML templates. |

## Time Constraints

| Risk | Impact | Mitigation |
|---|---|---|
| 15-week deadline | High | Strict MVP boundary prevents scope creep. Weekly deliverables keep the project on track. |
| Learning curve for Jenkins/Docker/Ansible | Medium | Use official documentation and simple configurations. |

## Technology Trade-Offs Summary

| Decision | Selected | Alternative | Trade-Off |
|---|---|---|---|
| Flask over Django | Flask | Django | Less scaffolding, but simpler for Docker/Jenkins. |
| SQLite over MySQL | SQLite | MySQL/PostgreSQL | No server to manage, but limited concurrency. |
| Ansible over Puppet | Ansible | Puppet | Agentless and simpler, but less enterprise tooling. |
| Gunicorn over Nginx+uWSGI | Gunicorn | Nginx+uWSGI | Single command, but no reverse proxy. |
| HTML/JS over React | HTML/CSS/JS | React/Angular | No build step, but less interactive UI. |
