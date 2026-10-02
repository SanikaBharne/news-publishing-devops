# Pull Request

## Overview

The Week 5 feature was developed on the `feature/article-submission` branch. After implementation and testing, the branch was pushed to the GitHub remote.

## Pull Request Details

| Field | Value |
|---|---|
| **Source Branch** | `feature/article-submission` |
| **Target Branch** | `development` |
| **PR Title** | *(Not yet created on GitHub)* |
| **PR Purpose** | Merge the article submission feature (POST /api/articles with validation, frontend form, and 6 pytest tests) into the development integration branch. |
| **Files/Features Included** | `src/app.py`, `src/templates/index.html`, `tests/test_submission.py`, `docs/week-05/*` |
| **PR Status** | **PENDING — GitHub PR has not been created yet.** |

## Current State

- The `feature/article-submission` branch **exists on the GitHub remote** (`remotes/origin/feature/article-submission`).
- A **local merge** into `development` was performed using `git merge --no-ff` (commit `c997ee6`), which preserves the branch history as if a PR merge had occurred.
- However, **no Pull Request has been opened on GitHub** as of this writing.

## Manual Action Required

To create the PR on GitHub:

1. Navigate to: `https://github.com/SanikaBharne/news-publishing-devops`
2. GitHub may show a banner: "feature/article-submission had recent pushes — Compare & pull request". Click it.
3. Set **base** to `development` and **compare** to `feature/article-submission`.
4. Title: `feat: add article submission and validation`
5. Description: Reference the feature requirements and list the files changed.
6. Click **Create pull request**.

Since the local `development` branch already contains the merged code and has been pushed, the PR may show as already merged or may need to be closed manually. The local merge commit (`c997ee6`) serves as the equivalent integration point.
