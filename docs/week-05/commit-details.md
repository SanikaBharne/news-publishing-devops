# Commit Details

## Commit Strategy

The Article Submission feature was committed to the isolated `feature/article-submission` branch using the conventional commit format defined in Week 4. Code changes and documentation changes were separated into distinct commits.

## Commits on `feature/article-submission`

### Commit 1: Feature Code

| Field | Value |
|---|---|
| **Hash** | `b59d710` |
| **Message** | `feat: add article submission and validation` |
| **Purpose** | Implement the article submission API endpoint, frontend form, and automated tests. |
| **Files** | `src/app.py` (modified), `src/templates/index.html` (new), `tests/test_submission.py` (new) |

### Commit 2: Documentation

| Field | Value |
|---|---|
| **Hash** | `a9ce133` |
| **Message** | `docs: add week 5 feature documentation` |
| **Purpose** | Add Week 5 documentation covering the feature, validation, testing, and Git workflow. |
| **Files** | `docs/week-05/*` (11 new files), `docs/evidence/week-05/evidence-checklist.md` (new) |

## Merge Commit

| Field | Value |
|---|---|
| **Hash** | `c997ee6` |
| **Message** | `Merge pull request #2 from feature/article-submission` |
| **Purpose** | Merge the completed feature branch into `development` using `--no-ff` to preserve branch history. |
| **Note** | This merge was performed locally. A GitHub Pull Request has not yet been created (see `pull-request.md`). |
