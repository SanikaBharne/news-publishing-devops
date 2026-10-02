# Technology Decisions

## 1. Backend Framework: Flask

| | |
|---|---|
| **Selected:** | Flask (Python) |
| **Alternatives:** | Django, FastAPI |
| **Reason:** | Flask is a lightweight microframework with minimal boilerplate, ideal for a small MVP. Django provides too much built-in scaffolding (admin panel, ORM) that is unnecessary for 5 API endpoints. FastAPI is excellent but async patterns add complexity for an academic project. |
| **Trade-off:** | Less built-in functionality, but simpler to learn, debug, and integrate with Docker/Jenkins. |

## 2. Database: SQLite

| | |
|---|---|
| **Selected:** | SQLite |
| **Alternatives:** | MySQL, PostgreSQL |
| **Reason:** | Zero-configuration, file-based storage, bundled with Python. No separate database server to install or manage. Perfectly suitable for a single-user academic MVP. |
| **Trade-off:** | Not suitable for concurrent writes at scale, but the MVP has no concurrent user requirement. |

## 3. Frontend: HTML/CSS/JS + Jinja2

| | |
|---|---|
| **Selected:** | Plain HTML/CSS/JS with Jinja2 server-side rendering |
| **Alternatives:** | React, Angular, Vue.js |
| **Reason:** | No frontend build step required (no Node.js, npm, webpack). Pages are served directly by Flask. This avoids frontend complexity that would distract from the DevOps focus. |
| **Trade-off:** | Less interactive UI, but sufficient for form submission and dashboard display. |

## 4. Configuration Management: Ansible

| | |
|---|---|
| **Selected:** | Ansible |
| **Alternatives:** | Puppet |
| **Reason:** | Agentless architecture (connects via SSH). No agent software needs to be installed on target machines. YAML-based playbooks are easier to write and read for a student project. |
| **Trade-off:** | Puppet has a more mature ecosystem for large-scale infrastructure, but Ansible is simpler for academic demonstrations. |

## 5. Deployment Server: Gunicorn

| | |
|---|---|
| **Selected:** | Gunicorn |
| **Alternatives:** | Nginx + uWSGI, Waitress |
| **Reason:** | Gunicorn is a standard WSGI server for Flask. Single command to run. Works well inside Docker containers. |
| **Trade-off:** | No built-in reverse proxy, but a reverse proxy is not required for the academic scope. |

## 6. Testing: pytest + Selenium

| | |
|---|---|
| **Selected:** | pytest (unit), Selenium WebDriver (UI) |
| **Alternatives:** | unittest, Robot Framework |
| **Reason:** | pytest has cleaner syntax and better fixture support than unittest. Selenium is required by the project scope for automated UI testing. |
| **Trade-off:** | Selenium tests can be flaky due to timing issues; explicit waits will be used. |

## What Is Intentionally Kept Simple
- Single database table (no users, roles, or categories).
- Author is a plain text string, not a foreign key.
- Role simulation via UI navigation rather than authentication.
- No HTTPS, session management, or CSRF protection in the MVP.
