# Week 6 Unit Testing Documentation

## Overview
Unit testing for Week 6 features was implemented using `pytest` and Flask's test client in `tests/test_reviewer.py`.

## Test Execution Command
```bash
python -m pytest -v
```

## Test Coverage Summary

| Test Case Name | Target Endpoint | Description | Expected Status Code | Result |
|---|---|---|---|---|
| `test_reviewer_dashboard_listing` | `GET /api/articles` | Verifies listing all articles for dashboard | 200 | PASSED |
| `test_approve_valid_submitted_article` | `PUT /api/articles/<id>/approve` | Approves a valid submitted article | 200 | PASSED |
| `test_verify_approval_status` | `GET /api/articles/<id>` | Verifies status is `APPROVED` after approval | 200 | PASSED |
| `test_reject_valid_submitted_article` | `PUT /api/articles/<id>/reject` | Rejects article with valid comment | 200 | PASSED |
| `test_verify_rejection_status_and_comment` | `GET /api/articles/<id>` | Verifies status is `REJECTED` and comment is stored | 200 | PASSED |
| `test_reject_without_comment` | `PUT /api/articles/<id>/reject` | Rejects without comment payload | 400 | PASSED |
| `test_reject_with_whitespace_comment` | `PUT /api/articles/<id>/reject` | Rejects with whitespace-only comment | 400 | PASSED |
| `test_invalid_article_id` | `PUT/GET /api/articles/999/*` | Verifies 404 behavior for invalid IDs | 404 | PASSED |

## Full Test Suite Verification
Total Tests Ran: 14 (6 submission tests + 8 reviewer tests)
Passing: 14/14 (100% pass rate)
