# API Testing

## Overview

The `POST /api/articles` endpoint was tested to verify correct behavior for both valid and invalid inputs. Testing was performed using the Flask test client through pytest (see `unit-testing.md` for automated test details). The scenarios below document the expected and actual behavior.

## Test 1: Valid Submission

**Input:**
```json
{
    "title": "Test Title",
    "content": "Test Content",
    "author": "Test Author"
}
```

**Expected:** HTTP `201 Created`, response contains `id`, `message`, and `status: "SUBMITTED"`.

**Actual:** HTTP `201 Created`. Response:
```json
{
    "message": "Article submitted successfully",
    "id": 1,
    "status": "SUBMITTED"
}
```

**Result:** ✅ PASS

## Test 2: Missing Title

**Input:**
```json
{
    "content": "Test Content",
    "author": "Test Author"
}
```

**Expected:** HTTP `400 Bad Request` with error message containing "required fields".

**Actual:** HTTP `400 Bad Request`. Response:
```json
{
    "error": "Title, content, and author are required fields and cannot be empty."
}
```

**Result:** ✅ PASS

## Test 3: Missing Content

**Input:**
```json
{
    "title": "Test Title",
    "author": "Test Author"
}
```

**Expected:** HTTP `400 Bad Request` with error message containing "required fields".

**Actual:** HTTP `400 Bad Request` with the same validation error message.

**Result:** ✅ PASS

## Test 4: Missing Author

**Input:**
```json
{
    "title": "Test Title",
    "content": "Test Content"
}
```

**Expected:** HTTP `400 Bad Request` with error message containing "required fields".

**Actual:** HTTP `400 Bad Request` with the same validation error message.

**Result:** ✅ PASS

## Test 5: Whitespace-Only Values

**Input:**
```json
{
    "title": "   ",
    "content": "Test Content",
    "author": "Test Author"
}
```

**Expected:** HTTP `400 Bad Request`. The `.strip()` call reduces `"   "` to `""`, which fails the `if not title` check.

**Actual:** HTTP `400 Bad Request` with the same validation error message.

**Result:** ✅ PASS

## Test 6: SUBMITTED Status After Successful Submission

**Input:**
```json
{
    "title": "Persistent Title",
    "content": "Persistent Content",
    "author": "Persistent Author"
}
```

**Expected:** The article is saved to SQLite with `status = "SUBMITTED"`.

**Actual:** Direct SQLite query on `test_app.db` confirmed the record exists with `title = "Persistent Title"` and `status = "SUBMITTED"`.

**Result:** ✅ PASS

## Summary

| Test Case | HTTP Status | Result |
|---|---|---|
| Valid submission | 201 | ✅ PASS |
| Missing title | 400 | ✅ PASS |
| Missing content | 400 | ✅ PASS |
| Missing author | 400 | ✅ PASS |
| Whitespace-only fields | 400 | ✅ PASS |
| Database persistence & SUBMITTED status | 201 | ✅ PASS |
