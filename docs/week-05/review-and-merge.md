# Review and Merge Process

## Expected GitHub Review Process
After the Pull Request is created:
1.  **Code Review:** A peer (or the author, for academic solo projects) reviews the code diff on GitHub to ensure it meets requirements and passes CI (when configured).
2.  **Merge:** Click the "Merge pull request" button on GitHub to merge the changes into the `development` branch.
3.  **Local Sync:** Return to the local terminal, checkout development, and pull the latest changes.
    ```bash
    git checkout development
    git pull origin development
    ```

## Local Simulation
To ensure the local repository reflects the completed feature for subsequent weeks, a local merge was performed:
```bash
git checkout development
git merge feature/article-submission --no-ff -m "Merge pull request #2 from feature/article-submission"
```
*(Note: If utilizing a remote GitHub repository, you should perform the merge on GitHub and pull it down, rather than merging locally).*
