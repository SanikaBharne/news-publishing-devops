# Validation Rules

## Overview

The `POST /api/articles` endpoint enforces server-side validation to ensure data integrity before any article is saved to the database. The validation logic is implemented in the `submit_article()` function in `src/app.py`.

## Rules

### 1. Required Title
- The `title` field must be present in the JSON payload.
- If omitted, `data.get('title', '')` defaults to an empty string, which fails the `if not title` check.

### 2. Required Content
- The `content` field must be present in the JSON payload.
- If omitted, validation fails with the same error message.

### 3. Required Author
- The `author` field must be present in the JSON payload.
- If omitted, validation fails with the same error message.

### 4. Reject Whitespace-Only Values
- Each field is processed with `.strip()` before validation.
- A value like `"   "` (spaces only) becomes `""` after stripping, which is treated as empty and rejected.
- This prevents articles from being submitted with blank titles, blank content, or blank authors.

### 5. No JSON Payload
- If the request body is empty or not valid JSON, `request.get_json()` returns `None`.
- This is caught by the `if not data` check, returning a `400` error with `"No JSON payload provided"`.

## Validation Response

When validation fails, the API returns:

- **HTTP Status:** `400 Bad Request`
- **JSON Body:**
  ```json
  {
      "error": "Title, content, and author are required fields and cannot be empty."
  }
  ```

When validation passes, the API returns:

- **HTTP Status:** `201 Created`
- **JSON Body:**
  ```json
  {
      "message": "Article submitted successfully",
      "id": 1,
      "status": "SUBMITTED"
  }
  ```
