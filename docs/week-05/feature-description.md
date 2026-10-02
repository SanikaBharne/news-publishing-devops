# Feature Description: Article Submission with Required-Field Validation

## Why Article Submission Is Needed

The News Publishing Workflow begins when a writer submits a news article for review. Without a submission mechanism, there is no content entering the pipeline and no work for reviewers, approvers, or the status-tracking system. Article submission is the foundational feature upon which all other MVP features depend.

## The Writer's Workflow

1. The writer navigates to the application's home page (`http://127.0.0.1:5000/`).
2. The writer fills in three required fields: **Title**, **Author**, and **Content**.
3. The writer clicks **Submit Article**.
4. The frontend sends a `POST /api/articles` request with JSON data to the Flask backend.
5. The backend validates the input.
6. If valid, the article is saved to the SQLite database with status `SUBMITTED` and the current timestamp as `submission_date`. The writer sees a success message with the article ID and status.
7. If invalid (missing or whitespace-only fields), the backend returns a `400 Bad Request` error with a clear message. The writer sees an error message on the form.

## Expected Valid Behavior

- All three fields (`title`, `content`, `author`) are provided and non-empty.
- The article is saved to the `articles` table in SQLite.
- The `status` column is set to `SUBMITTED`.
- The `submission_date` column is set to the current UTC timestamp.
- The API returns HTTP `201 Created` with a JSON body containing `id`, `message`, and `status`.

## Expected Invalid Behavior

- If any of the three required fields is missing from the JSON payload, the API returns HTTP `400 Bad Request`.
- If any field contains only whitespace characters (e.g., `"   "`), the value is stripped and treated as empty, triggering a `400` error.
- If no JSON payload is provided at all, the API returns HTTP `400 Bad Request`.
- The error response includes a clear message: `"Title, content, and author are required fields and cannot be empty."`
