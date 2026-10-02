# .gitignore Strategy

## Purpose
The `.gitignore` file tells Git which files and directories to ignore and not track in version control. This prevents unnecessary, temporary, or sensitive files from cluttering the repository.

## Python/Flask Exclusions
The project uses a standard Python `.gitignore` template. Key exclusions include:

*   **Byte-compiled files:** `__pycache__/`, `*.pyc`, `*.pyo`
    *   *Reason:* Generated automatically by Python; not source code.
*   **Virtual Environments:** `venv/`, `.venv/`, `env/`
    *   *Reason:* Dependencies are defined in `requirements.txt`; the virtual environment folder is large and environment-specific.
*   **Cache files:** `.pytest_cache/`
    *   *Reason:* Testing cache, recreated on each test run.
*   **Local environment variables:** `.env`
    *   *Reason:* May contain sensitive secrets (though not used in this MVP).
*   **IDE/editor files:** `.vscode/`, `.idea/`
    *   *Reason:* Developer-specific settings that shouldn't be shared.
*   **Local Database:** `*.sqlite3`
    *   *Reason:* Excluded to prevent committing local development test data. A fresh database will be generated or mocked in CI.

## Files Intentionally NOT Ignored
The following files are critical for reproducibility and MUST be committed:
*   `requirements.txt`: Needed to install dependencies.
*   `docs/*`: Project documentation is a core deliverable.
*   `src/*`: Application source code.
*   `README.md`: Project overview.
