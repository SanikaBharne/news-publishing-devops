# Git Branch Workflow

Following the Week 4 branching strategy, all Week 5 feature development occurred in isolation to prevent breaking the `development` integration branch.

## Workflow Execution
1.  **Branch Check:** Verified current status with `git status` and `git branch -a`.
2.  **Base Setup:** Checked out the `development` branch.
    ```bash
    git checkout development
    git pull origin development
    ```
3.  **Feature Branch Creation:** Created a new, isolated branch specifically for this task.
    ```bash
    git checkout -b feature/article-submission
    ```
4.  **Implementation:** Application code, HTML templates, and tests were written.
5.  **Staging and Committing:** Code was staged and committed with conventional commit messages (see commit-details.md).
