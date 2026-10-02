# API Testing Details

Manual testing of the API ensures that it behaves correctly under different conditions. (Automated testing is covered in unit-testing.md).

## Test Cases Executed Locally

### 1. Valid Submission
**Request:**
```json
{
  "title": "Breaking News",
  "content": "This is the content of the news.",
  "author": "Jane Doe"
}
```
**Response (201 Created):**
```json
{
  "id": 1,
  "message": "Article submitted successfully",
  "status": "SUBMITTED"
}
```

### 2. Missing Fields
**Request:**
```json
{
  "title": "Breaking News",
  "author": "Jane Doe"
}
```
**Response (400 Bad Request):**
```json
{
  "error": "Title, content, and author are required fields and cannot be empty."
}
```

### 3. Whitespace-Only Submission
**Request:**
```json
{
  "title": "   ",
  "content": "Content here",
  "author": "Jane Doe"
}
```
**Response (400 Bad Request):** Validation catches the stripped title and rejects the payload.
