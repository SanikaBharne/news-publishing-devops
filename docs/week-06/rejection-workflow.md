# Rejection Workflow Documentation

## Endpoint Definition
- **Method**: `PUT`
- **Path**: `/api/articles/<id>/reject`
- **Payload**:
```json
{
  "comment": "Article requires factual corrections."
}
```

## Validation & Business Rules
1. **Mandatory Rejection Comment**:
   - `comment` field must be present in JSON payload.
   - Comment cannot be empty or contain whitespace only (`comment.strip()` check).
   - If comment validation fails, returns HTTP 400 with message: `"Rejection comment is mandatory and cannot be empty."`.
2. **Article Existence**: Returns HTTP 404 if article `<id>` does not exist.
3. **Status Check**: Only `SUBMITTED` articles can be rejected. Returns HTTP 400 if article is already `APPROVED` or `REJECTED`.
4. **State Transition**:
   - `status` → `REJECTED`
   - `comment` → Stored rejection comment
   - `review_date` → Current UTC timestamp

## Responses
- **Success (HTTP 200)**:
```json
{
  "id": 1,
  "message": "Article rejected successfully",
  "status": "REJECTED"
}
```
- **Invalid Comment / Missing Body (HTTP 400)**:
```json
{
  "error": "Rejection comment is mandatory and cannot be empty."
}
```
- **Article Not Found (HTTP 404)**:
```json
{
  "error": "Article not found"
}
```
