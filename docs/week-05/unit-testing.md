# Unit Testing

## Overview

Automated unit tests were written using `pytest` to verify the article submission endpoint. The test file is located at `tests/test_submission.py`.

## Test Configuration

A `client` pytest fixture creates a Flask test client. The fixture:

1. Sets `app.config['TESTING'] = True`.
2. Patches the `DATABASE` variable to use `test_app.db` instead of `app.db` to isolate test data from the development database.
3. Calls `init_db()` within the app context to create the `articles` table in the test database.
4. Yields the Flask test client for use in test functions.
5. Removes `test_app.db` after tests complete (cleanup).

## Test Cases

| # | Test Function | Purpose | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| 1 | `test_valid_submission` | Verify successful article submission | `{"title": "Test Title", "content": "Test Content", "author": "Test Author"}` | 201 Created, response contains `id` and `status: "SUBMITTED"` | 201 Created, all assertions passed | ✅ PASS |
| 2 | `test_missing_title` | Verify rejection when title is missing | `{"content": "Test Content", "author": "Test Author"}` | 400 Bad Request, error contains "required fields" | 400 Bad Request, assertion passed | ✅ PASS |
| 3 | `test_missing_content` | Verify rejection when content is missing | `{"title": "Test Title", "author": "Test Author"}` | 400 Bad Request, error contains "required fields" | 400 Bad Request, assertion passed | ✅ PASS |
| 4 | `test_missing_author` | Verify rejection when author is missing | `{"title": "Test Title", "content": "Test Content"}` | 400 Bad Request, error contains "required fields" | 400 Bad Request, assertion passed | ✅ PASS |
| 5 | `test_whitespace_only_fields` | Verify rejection of whitespace-only title | `{"title": "   ", "content": "Test Content", "author": "Test Author"}` | 400 Bad Request, error contains "required fields" | 400 Bad Request, assertion passed | ✅ PASS |
| 6 | `test_database_persistence_and_status` | Verify article is saved to SQLite with correct status | `{"title": "Persistent Title", "content": "Persistent Content", "author": "Persistent Author"}` | Record found in DB with `status = "SUBMITTED"` | Record found, `title` and `status` match | ✅ PASS |

## Execution

**Command:**
```bash
python -m pytest -v
```

**Result:**
```
tests/test_submission.py::test_valid_submission PASSED
tests/test_submission.py::test_missing_title PASSED
tests/test_submission.py::test_missing_content PASSED
tests/test_submission.py::test_missing_author PASSED
tests/test_submission.py::test_whitespace_only_fields PASSED
tests/test_submission.py::test_database_persistence_and_status PASSED

6 passed, 2 warnings in 0.55s
```

**Warnings:** Two `DeprecationWarning` notices about `datetime.datetime.utcnow()` being deprecated in favor of timezone-aware objects. These are non-critical and do not affect functionality.
