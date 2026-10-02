# Git Verification

The following Git commands were executed during Week 4 to verify the local Git repository setup and branching demonstration.

| Command | Purpose | Actual Result | Status |
| :--- | :--- | :--- | :--- |
| `git --version` | Verify Git installation | `git version 2.52.0.windows.1` | ✅ PASS |
| `git init` | Initialize repository | `Initialized empty Git repository...` | ✅ PASS |
| `git status` | Check working tree status | `On branch development... nothing to commit` | ✅ PASS |
| `git branch` | List local branches | `* development`, `feature/week4-git-setup`, `main` | ✅ PASS |
| `git log --oneline` | View commit history | History shows initial commits and the merge commit. | ✅ PASS |
| `git remote -v` | Check remote repositories | *(Blank output - remote not yet added)* | ⏳ PENDING (Manual step) |
| `git checkout -b <branch>` | Create and switch branch | `Switched to a new branch 'development'` | ✅ PASS |
| `git merge <branch> --no-ff` | Simulate PR merge | `Merge made by the 'ort' strategy.` | ✅ PASS |
