# Week 5 Summary: Article Submission with Required-Field Validation

## Objective

Implement the first core application MVP feature — article submission with server-side required-field validation — following the Git branching strategy and commit convention established in Week 4.

## Feature Developed

A `POST /api/articles` endpoint was built in Flask that accepts a JSON payload with `title`, `content`, and `author` fields. Valid submissions are saved to a local SQLite database (`app.db`) with the status `SUBMITTED` and the current UTC timestamp as the `submission_date`. A simple HTML frontend form was also created to allow users to interact with the endpoint via a browser.

## Validation Implemented

- All three fields (`title`, `content`, `author`) are required.
- Each field is sanitized with `.strip()` to reject whitespace-only values.
- Missing or empty fields return HTTP `400 Bad Request` with a clear error message.
- Missing JSON payload returns HTTP `400 Bad Request`.

## Tests Performed

Six `pytest` unit tests were written in `tests/test_submission.py`:

1. `test_valid_submission` — verifies 201 response and correct JSON structure.
2. `test_missing_title` — verifies 400 when title is omitted.
3. `test_missing_content` — verifies 400 when content is omitted.
4. `test_missing_author` — verifies 400 when author is omitted.
5. `test_whitespace_only_fields` — verifies whitespace-only title is rejected.
6. `test_database_persistence_and_status` — verifies the article is saved in SQLite with `status = "SUBMITTED"`.

**Result:** All 6 tests passed (`python -m pytest -v` → `6 passed, 2 warnings in 0.55s`).

## Git Branching Workflow

1. Checked out `development` and pulled the latest from `origin/development`.
2. Created `feature/article-submission` from `development`.
3. Committed feature code: `b59d710 feat: add article submission and validation`.
4. Committed documentation: `a9ce133 docs: add week 5 feature documentation`.
5. Pushed `feature/article-submission` to GitHub.
6. Merged locally into `development` using `--no-ff` (commit `c997ee6`).

## PR and Merge

- The `feature/article-submission` branch was pushed to the GitHub remote.
- A **GitHub Pull Request has not yet been created** on the repository. The merge was performed locally.
- The local `development` branch contains all Week 5 changes and has a clean working tree.

## Final Outcome

The article submission feature is fully implemented, tested, and merged into the local `development` branch. The application can:

- Accept valid article submissions and save them to SQLite.
- Reject invalid or incomplete submissions with clear error messages.
- Display a frontend form for manual submission.

**Week 5 is complete. Week 6 will continue MVP development (reviewer dashboard, approval, rejection, status tracking). No MVP features beyond article submission were implemented in Week 5.**
