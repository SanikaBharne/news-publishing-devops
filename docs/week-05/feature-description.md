# Feature Description: Article Submission

## Overview
The goal of Week 5 is to implement the first core application feature: Article Submission with Required-Field Validation. This represents the beginning of the "News Publishing Workflow".

## Requirements
*   **Endpoint:** `POST /api/articles`
*   **Purpose:** Allows writers to submit a news article for review.
*   **Inputs (JSON):**
    *   `title` (String)
    *   `content` (String)
    *   `author` (String)
*   **Outputs (JSON):**
    *   Success (201 Created): Returns `{ "message": "...", "id": <db_id>, "status": "SUBMITTED" }`
    *   Error (400 Bad Request): Returns `{ "error": "..." }`

## Expected Behavior
When valid data is submitted, the backend must save the article to the SQLite database with the status explicitly set to `SUBMITTED`, and record the current timestamp as the `submission_date`.
