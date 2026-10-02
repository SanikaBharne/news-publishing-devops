# Pull Request Documentation – Week 6

## Pull Request Details
- **Title**: `feat: add reviewer workflow, approval/rejection endpoints, and UI dashboard`
- **Head Branch**: `feature/reviewer-workflow`
- **Base Branch**: `development`
- **Repository**: `https://github.com/SanikaBharne/news-publishing-devops`

## Description of Changes
1. **Reviewer Dashboard**:
   - Web interface at `/reviewer` displaying submitted articles with ID, title, author, submission date, and status.
   - Interactive detail modal allowing reviewers to inspect content and execute review actions.
2. **Approval Endpoint**:
   - `PUT /api/articles/<id>/approve` transitions status from `SUBMITTED` to `APPROVED` and records `review_date`.
3. **Rejection Endpoint**:
   - `PUT /api/articles/<id>/reject` validates mandatory rejection comment, transitions status to `REJECTED`, and records comment + `review_date`.
4. **Status Tracking**:
   - Full article status details returned via `GET /api/articles/<id>`.
5. **Automated Testing**:
   - 8 unit test cases in `tests/test_reviewer.py` covering positive/negative validation flows and DB persistence.

## Verification Checklist
- [x] All 14 pytest unit tests passing.
- [x] Tested manual UI flows for approval and rejection.
- [x] Mandatory rejection comment validation verified (rejecting without comment returns 400).
- [x] Clean REST error handling (404 for invalid IDs, 400 for bad state or missing comments).
