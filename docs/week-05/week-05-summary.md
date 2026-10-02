# Week 5 Summary: Article Submission Feature

## Objective
Implement the first application MVP feature: Article Submission with Required-Field Validation.

## Work Completed
- Built `POST /api/articles` endpoint in Flask.
- Implemented SQLite database initialization and data persistence for articles.
- Implemented business logic validating that `title`, `content`, and `author` are present and not empty strings.
- Built a simple frontend HTML form (`src/templates/index.html`) using the Fetch API to interact with the backend.
- Created robust unit tests using `pytest` to cover success, validation errors, and database persistence.
- Executed all work on a dedicated `feature/article-submission` branch.

## Testing Results
- `python -m pytest` was executed successfully. 6 tests passed covering all acceptance criteria.

## Git Workflow
- Branched off `development`.
- Committed code using `feat: add article submission and validation`.
- Documented manual steps required for GitHub PR creation and merging.

## Pending Manual Actions
To fully complete Week 5 on the remote repository, the user must manually:
1. `git push -u origin feature/article-submission`
2. Create a Pull Request into `development` on GitHub.
3. Review and Merge the PR on GitHub.
4. Update local `development` via `git checkout development && git pull`.
