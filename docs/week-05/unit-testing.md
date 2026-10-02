# Unit Testing

To ensure the Article Submission workflow remains stable in the CI/CD pipeline, `pytest` unit tests were implemented.

## Test File
*   `tests/test_submission.py`

## Test Setup (Fixtures)
*   A `client` fixture was created to inject a Flask test client.
*   The application was pointed to an in-memory or isolated test database (`test_app.db`) to prevent contaminating the local development database.

## Tests Written
1.  **`test_valid_submission`**: Verifies a 201 response and correct JSON structure on success.
2.  **`test_missing_title`**: Verifies a 400 response when the title is omitted.
3.  **`test_missing_content`**: Verifies a 400 response when the content is omitted.
4.  **`test_missing_author`**: Verifies a 400 response when the author is omitted.
5.  **`test_whitespace_only_fields`**: Verifies that spacing-only inputs trigger validation.
6.  **`test_database_persistence_and_status`**: Connects directly to the test SQLite database to verify the record was saved with the exact text and the status `SUBMITTED`.

## Execution Results
Command: `python -m pytest`
Result: `6 passed`
