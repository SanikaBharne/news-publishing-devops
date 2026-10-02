# Implementation Details

## Flask Backend Implementation

### Database Layer (`src/app.py`)

The application uses Python's built-in `sqlite3` module to interact with a local SQLite database file (`app.db`). Key implementation details:

- **Connection management:** The `get_db()` function stores the database connection on Flask's `g` application context object, ensuring one connection per request. The `close_connection()` teardown function closes the connection automatically when the request ends.
- **Schema initialization:** The `init_db()` function creates the `articles` table if it does not already exist. This function is called when the application starts via `if __name__ == '__main__'`.
- **Table schema:**
  ```sql
  CREATE TABLE IF NOT EXISTS articles (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      content TEXT NOT NULL,
      author TEXT NOT NULL,
      status TEXT NOT NULL,
      comment TEXT,
      submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
      review_date TIMESTAMP
  )
  ```

### API Endpoint (`POST /api/articles`)

The `submit_article()` function handles article submission:

1. Parses the incoming JSON payload using `request.get_json()`.
2. Extracts `title`, `content`, and `author`, applying `.strip()` to each value.
3. Validates that all three fields are non-empty after stripping.
4. If validation fails, returns `400 Bad Request` with an error message.
5. If validation passes, inserts the article into the database with status `SUBMITTED` and the current UTC timestamp.
6. Returns `201 Created` with the new article's `id` and `status`.

### Frontend (`src/templates/index.html`)

A simple HTML page rendered via Jinja2 (`render_template('index.html')`) at the root route (`/`). The page contains:

- A form with three input fields: Title, Author, and Content.
- A submit button.
- A message `<div>` that dynamically displays success (green) or error (red) messages.
- Vanilla JavaScript using the `fetch` API to send a JSON `POST` request and process the response without page reload.

## Files Changed in Week 5

| File | Change |
|---|---|
| `src/app.py` | Replaced minimal health-check skeleton with full SQLite setup, `init_db()`, `get_db()`, `close_connection()`, `/` route, and `POST /api/articles` endpoint. |
| `src/templates/index.html` | New file. Frontend submission form with JavaScript fetch logic. |
| `tests/test_submission.py` | New file. Six pytest test cases for the submission endpoint. |
