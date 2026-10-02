# Git Branching Strategy

For this academic DevOps project, we use a simplified branching strategy that simulates professional workflows without unnecessary complexity.

## Branch Hierarchy

1.  **`main` Branch**
    *   **Purpose:** The stable, production-ready codebase.
    *   **Rules:**
        *   No direct commits allowed.
        *   Only merges from `development` are accepted.
        *   In later weeks, this branch will trigger the automated deployment pipeline to production.

2.  **`development` Branch**
    *   **Purpose:** The main integration branch for active development.
    *   **Rules:**
        *   Created by branching off `main`.
        *   All feature branches merge into this branch.
        *   This branch is used for testing features together before release.

3.  **`feature/*` Branches**
    *   **Purpose:** Development of individual features, bug fixes, or documentation tasks.
    *   **Rules:**
        *   Created by branching off `development`.
        *   Must follow the naming convention `feature/<feature-name>`.
        *   Example: `feature/article-submission`, `feature/reviewer-dashboard`.
        *   Should be merged back into `development` via a Pull Request (PR) when complete.

## Workflow Example

1.  Create a feature branch from development:
    ```bash
    git checkout development
    git pull origin development
    git checkout -b feature/article-submission
    ```
2.  Work on the feature and make commits.
3.  Push the feature branch to GitHub:
    ```bash
    git push -u origin feature/article-submission
    ```
4.  Open a Pull Request on GitHub from `feature/article-submission` to `development`.
5.  Review and merge the PR.
6.  Once all features for a week/release are in `development` and tested, merge `development` into `main`.

## Pull Request Expectations
*   Provide a clear summary of changes.
*   Link to any relevant GitHub Issues.
*   Ensure all tests pass before merging (once CI is set up).
