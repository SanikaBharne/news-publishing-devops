# Validation Rules

The following business rules were implemented to ensure data integrity during article submission.

1.  **JSON Payload Requirement:** The API explicitly checks if a JSON payload was provided.
2.  **Field Presence:** `title`, `content`, and `author` must all be present in the request body.
3.  **No Empty Strings:** Fields are checked against being purely empty strings `""`.
4.  **No Whitespace Strings:** Input fields are sanitized using `.strip()`. If a user submits `"   "`, it resolves to an empty string and triggers a validation error.

*Error Response:*
If any of these conditions fail, the application returns a `400 Bad Request` with the message: `"Title, content, and author are required fields and cannot be empty."`
