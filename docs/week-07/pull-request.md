# Pull Request Documentation – Week 7

## Pull Request Details
- **Title**: `ci: add Jenkins pipeline and CI documentation`
- **Head Branch**: `feature/jenkins-ci`
- **Base Branch**: `development`
- **Repository**: `https://github.com/SanikaBharne/news-publishing-devops`

## Description of Changes
1. **Continuous Integration Pipeline**:
   - Added `Jenkinsfile` at the repository root.
   - Configured stages: Checkout SCM, Install Dependencies (via Python `venv`), and Run Tests (`pytest`).
2. **Documentation**:
   - Added comprehensive documentation in `docs/week-07/` detailing Jenkins installation, job configuration, pipeline structure, and testing outcomes.
   - Prepared `evidence-checklist.md` for tracking required empirical evidence.

## Verification Checklist
- [x] `Jenkinsfile` is syntactically correct and properly structures the pipeline stages.
- [x] The pipeline successfully executes `python -m pytest -v`, and all 14 tests pass.
- [x] Jenkins successfully reports the build status as SUCCESS.
