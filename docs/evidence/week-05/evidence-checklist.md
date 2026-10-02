# Week 5 Evidence Checklist

All screenshots below must be captured manually. None have been captured yet.

| Evidence ID | Screenshot | What Should Be Visible | Why It Is Evidence | Required | Status |
|---|---|---|---|---|---|
| W5_01 | `W5_01_Feature_Requirement.png` | The Week 5 feature requirement (e.g., `docs/week-05/feature-description.md` open in IDE, or a GitHub Issue describing article submission). | Proves that the feature was defined before implementation. | Yes | ⬜ PENDING |
| W5_02 | `W5_02_Feature_Branch.png` | Terminal output of `git branch` or `git log --oneline --graph` showing `feature/article-submission` exists alongside `development` and `main`. | Proves the branching strategy was followed. | Yes | ⬜ PENDING |
| W5_03 | `W5_03_Article_Submission_Form.png` | The browser at `http://127.0.0.1:5000/` showing the "Submit a News Article" form with Title, Author, and Content fields. | Proves the frontend was implemented and renders correctly. | Yes | ⬜ PENDING |
| W5_04 | `W5_04_Valid_Submission.png` | The browser showing the green success message after submitting a valid article (e.g., "Success! Article ID: 1, Status: SUBMITTED"). | Proves valid submission works end-to-end. | Yes | ⬜ PENDING |
| W5_05 | `W5_05_Invalid_Submission.png` | The browser or API client showing a red error message or 400 response when a required field is missing or empty. | Proves validation rejects invalid input. | Yes | ⬜ PENDING |
| W5_06 | `W5_06_Database_Article.png` | An SQLite viewer (e.g., DB Browser for SQLite, or terminal `sqlite3 app.db "SELECT * FROM articles;"`) showing a saved article row with `status = "SUBMITTED"`. | Proves data persistence and correct status assignment. | Yes | ⬜ PENDING |
| W5_07 | `W5_07_Pytest_Result.png` | Terminal output of `python -m pytest -v` showing all 6 test cases passing. | Proves automated testing was performed and passed. | Yes | ⬜ PENDING |
| W5_08 | `W5_08_Git_Status.png` | Terminal output of `git status` showing a clean working tree on the `development` branch. | Proves all changes were committed and the working tree is clean. | Yes | ⬜ PENDING |
| W5_09 | `W5_09_Git_Commit.png` | Terminal output of `git log --oneline -n 5` showing the `feat:` and `docs:` commits with their hashes. | Proves the commit convention was followed. | Yes | ⬜ PENDING |
| W5_10 | `W5_10_GitHub_Feature_Branch.png` | The GitHub repository page showing the `feature/article-submission` branch in the branch dropdown or branch list. | Proves the feature branch was pushed to GitHub. | Yes | ⬜ PENDING |
| W5_11 | `W5_11_Pull_Request.png` | The GitHub Pull Request page showing a PR from `feature/article-submission` to `development`. | Proves a PR was created on GitHub. | Yes (if PR exists) | ⬜ PENDING |
| W5_12 | `W5_12_PR_Review.png` | The GitHub PR review tab or conversation showing review activity. | Proves the PR was reviewed. | Yes (if PR exists) | ⬜ PENDING |
| W5_13 | `W5_13_PR_Merged.png` | The GitHub PR page showing a purple "Merged" badge. | Proves the PR was merged on GitHub. | Yes (if PR exists) | ⬜ PENDING |
| W5_14 | `W5_14_Development_Branch.png` | Terminal output of `git log --oneline --graph -n 5` on the `development` branch showing the merge commit. | Proves the feature was integrated into development. | Yes | ⬜ PENDING |
| W5_15 | `W5_15_Week5_Completion.png` | File Explorer or IDE showing the `docs/week-05/` folder contents with all documentation files. | Proves Week 5 documentation is complete. | Yes | ⬜ PENDING |

## Notes

- Screenshots W5_11, W5_12, and W5_13 require a GitHub Pull Request to exist. As of this writing, no PR has been created on GitHub for `feature/article-submission`. You must create the PR manually before capturing these screenshots.
- To run the app for screenshots W5_03, W5_04, and W5_05: `python src/app.py` then open `http://127.0.0.1:5000/` in a browser.
- For screenshot W5_06, use `sqlite3 app.db "SELECT * FROM articles;"` in the terminal, or use DB Browser for SQLite.
