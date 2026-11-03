# Dockerfile Explanation

The root `Dockerfile` packages the existing Flask app without changing its routes or templates.

- `python:3.12-slim` is a small, stable Python Linux base.
- `WORKDIR /app` gives commands a predictable working directory.
- `requirements.txt` is copied and installed before the source, so source-only changes can reuse the dependency layer.
- Only `src/` is copied. `.dockerignore` omits local databases, development tools, tests, documentation, secrets, and caches from the build context.
- The image runs as the unprivileged `appuser`; `/data` is writable by that user for SQLite.
- Gunicorn serves the Flask WSGI application on `0.0.0.0:5001`, using two workers and container stdout/stderr for logs. The startup command initializes the existing database schema before starting Gunicorn.
- Docker's health check uses Python's standard-library `urllib` to request `/health`, avoiding an extra curl package.
- `DATABASE_PATH=/data/app.db` is the container default. Outside the container, the existing relative `app.db` default remains unchanged.

The Dockerfile has been written but not built: the Docker CLI is present, but its Linux engine was unavailable during this work.
