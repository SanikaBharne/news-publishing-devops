# Pull Request Workflow

## Overview
This document outlines the standard Pull Request (PR) workflow used to integrate code into the `development` branch.

## The Workflow
The following steps represent the ideal PR lifecycle:

1.  **Feature Branch:** Developer creates a branch off `development` (e.g., `feature/article-submission`).
2.  **Commit:** Developer commits changes locally following the Commit Convention.
3.  **Push:** Developer pushes the branch to GitHub.
4.  **Pull Request:** Developer opens a Pull Request on GitHub from `feature/*` to `development`.
5.  **Review:** Another team member reviews the code, or self-review is performed if working solo.
6.  **Merge:** The PR is merged into `development` on GitHub.
7.  **Clean up:** The feature branch is deleted remotely and locally.

## Week 4 Demonstration
Since a GitHub remote could not be configured (requires actual user credentials), the Pull Request workflow was demonstrated locally using Git merge:

1.  Created branch `feature/week4-git-setup`.
2.  Committed a documentation change.
3.  Switched back to `development`.
4.  Performed a non-fast-forward merge to simulate a PR merge commit:
    ```bash
    git merge feature/week4-git-setup --no-ff -m "Merge pull request #1 from feature/week4-git-setup"
    ```
5.  This created a distinct merge commit, correctly simulating how a GitHub PR merge appears in Git history.
