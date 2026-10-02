# Pull Request Workflow

## Expected GitHub Workflow
Once the local feature branch is finalized, the following steps are required to create a Pull Request on GitHub:

1.  **Push Branch:** The branch must be pushed to the remote repository.
    ```bash
    git push -u origin feature/article-submission
    ```
2.  **Open PR:** Navigate to the GitHub repository online. Click "Compare & pull request".
3.  **Target Branch:** Set the base branch to `development` and the compare branch to `feature/article-submission`.
4.  **Description:** Provide a description referencing the Issue ("Closes #1: Implement Article Submission").

## Current Status (Manual Action Required)
Because GitHub authentication and web-ui interaction cannot be fully automated from this environment, **creating the actual PR on GitHub is pending manual user action.** Please execute the push command above and create the PR through the GitHub interface.
