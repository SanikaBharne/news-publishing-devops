# Git Setup

## Overview
This document records the initial Git setup for the project.

## Installation and Version
The project uses Git for version control.
*   **Command:** `git --version`
*   **Actual Result:** `git version 2.52.0.windows.1`

## Repository Initialization
The local directory was initialized as a Git repository.
*   **Command:** `git init`
*   **Result:** `Initialized empty Git repository in C:/Users/Sanika/Downloads/DevopsProject/.git/`

## Configuration
Local repository configuration was set for commits.
*   **Commands:**
    ```bash
    git config user.name "Student"
    git config user.email "student@example.com"
    ```

## Initial Git Status
Before the first commit, `git status` showed untracked files for the initial structure.
*   **Command:** `git status`
*   **Result snippet:** Untracked files included `.gitignore`, `requirements.txt`, `src/app.py`, and `docs/`.

## Initial Commit
The initial baseline of the project was committed.
*   **Command:** `git add .gitignore requirements.txt src/; git commit -m "chore: initialize git repository and project structure"`
*   **Result:** `[master (root-commit) dea804b] chore: initialize git repository and project structure`

*(Note: The default branch `master` was later renamed to `main` using `git branch -m master main`)*.
