# Implementation Details

## Backend (Flask)
*   **Database Setup:** SQLite is configured to store data in a local file (`app.db`). A table `articles` is created upon application startup if it doesn't already exist.
*   **Schema mapping:**
    *   `id`: AUTOINCREMENT PRIMARY KEY
    *   `title`: TEXT NOT NULL
    *   `content`: TEXT NOT NULL
    *   `author`: TEXT NOT NULL
    *   `status`: TEXT NOT NULL
    *   `submission_date`: TIMESTAMP
    *   `comment`: TEXT (for later use)
    *   `review_date`: TIMESTAMP (for later use)
*   **API Logic:** The `/api/articles` endpoint listens for `POST` requests, extracts JSON data, sanitizes it using `.strip()`, validates it, and executes an `INSERT INTO` SQL command.

## Frontend (HTML/JS)
*   A minimal, vanilla HTML form (`src/templates/index.html`) was created to allow users to interact with the API without needing tools like Postman or cURL.
*   The frontend uses the native `fetch` API to send a JSON payload and dynamically update a message box with the success or error response from the backend.
