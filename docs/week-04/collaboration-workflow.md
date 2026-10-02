# Collaboration Workflow

## Overview
This document outlines how team members (or a solo developer acting professionally) should collaborate on the codebase.

## Standard Development Cycle

1.  **Pull Latest Code:** Always start by ensuring your local `development` branch is up to date.
    ```bash
    git checkout development
    git pull origin development
    ```
2.  **Create Feature Branch:** Create a new branch for the specific issue you are working on.
    ```bash
    git checkout -b feature/<issue-name>
    ```
3.  **Make Changes:** Write code, update documentation, or add tests.
4.  **Test Locally:** Run the application locally and execute `pytest` to ensure no errors were introduced.
5.  **Commit:** Group changes logically and use the defined commit message convention.
    ```bash
    git commit -m "feat: add submit endpoint"
    ```
6.  **Push:** Push the feature branch to the remote repository.
    ```bash
    git push -u origin feature/<issue-name>
    ```
7.  **Create PR:** Open a Pull Request on GitHub against the `development` branch.
8.  **Review:** Request review. Address any feedback by pushing new commits to the same branch.
9.  **Merge:** Once approved and tests pass, merge the PR into `development`.
10. **Clean Up:** Delete the feature branch locally and remotely.
    ```bash
    git checkout development
    git pull origin development
    git branch -d feature/<issue-name>
    ```
