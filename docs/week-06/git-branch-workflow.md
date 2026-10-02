# Git Branch Workflow Documentation – Week 6

## Branching Strategy
Week 6 development followed the standard project Git branching strategy:
- `main`: Release-ready production branch.
- `development`: Main integration branch.
- `feature/reviewer-workflow`: Dedicated short-lived feature branch created from `development`.

## Workflow Steps Executed
1. **Branch Creation**:
   ```bash
   git checkout development
   git checkout -b feature/reviewer-workflow
   ```
2. **Feature Implementation & Testing**:
   - Backend routes added to `src/app.py`.
   - UI template added to `src/templates/reviewer.html`.
   - Unit tests added to `tests/test_reviewer.py`.
3. **Commit History**:
   - Commits created on `feature/reviewer-workflow` with standard Conventional Commit prefixes (`feat:`, `test:`, `docs:`).
4. **Integration**:
   - Pushed to remote: `git push origin feature/reviewer-workflow`.
   - Merged locally into `development` using `--no-ff` merge commit.
   - Pushed `development` to remote `origin/development`.
