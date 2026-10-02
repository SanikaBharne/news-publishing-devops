# Git Branch Workflow

## Overview

Following the branching strategy defined in Week 4, all Week 5 feature development was performed on an isolated feature branch. No code was committed directly to `main` or `development`.

## Workflow Executed

```
development (base)
    │
    ├── git checkout development
    ├── git pull origin development
    │
    └── git checkout -b feature/article-submission
            │
            ├── Implementation
            │   ├── Modified src/app.py
            │   ├── Created src/templates/index.html
            │   └── Created tests/test_submission.py
            │
            ├── Testing
            │   └── python -m pytest (6 passed)
            │
            ├── git add src/app.py src/templates/index.html tests/test_submission.py
            ├── git commit -m "feat: add article submission and validation"
            │
            ├── git add docs/week-05/ docs/evidence/week-05/
            ├── git commit -m "docs: add week 5 feature documentation"
            │
            ├── git push -u origin feature/article-submission
            │   (branch pushed to GitHub remote)
            │
            ├── GitHub Pull Request (PENDING — see pull-request.md)
            │
            └── Local merge into development
                ├── git checkout development
                └── git merge feature/article-submission --no-ff
                    (merge commit: c997ee6)
```

## Actual Commands Executed

1. **Update development:**
   ```bash
   git checkout development
   git pull origin development
   ```

2. **Create feature branch:**
   ```bash
   git checkout -b feature/article-submission
   ```

3. **Stage and commit code:**
   ```bash
   git add src/app.py src/templates/index.html tests/test_submission.py
   git commit -m "feat: add article submission and validation"
   ```

4. **Stage and commit documentation:**
   ```bash
   git add docs/week-05/ docs/evidence/week-05/
   git commit -m "docs: add week 5 feature documentation"
   ```

5. **Local merge into development:**
   ```bash
   git checkout development
   git merge feature/article-submission --no-ff -m "Merge pull request #2 from feature/article-submission"
   ```
