# Approval Workflow Documentation

## Endpoint Definition
- **Method**: `PUT`
- **Path**: `/api/articles/<id>/approve`
- **Payload**: None required.

## Validation & Workflow Rules
1. **Article Existence**: Checks if article `<id>` exists in SQLite database. Returns HTTP 404 if not found.
2. **Current Status Check**: Only articles with status `SUBMITTED` can be approved. Returns HTTP 400 if article is in any other status.
3. **State Transition**:
   - `status` → `APPROVED`
   - `review_date` → Current UTC timestamp (`YYYY-MM-DD HH:MM:SS`)
4. **Database Commit**: State changes are atomically committed to SQLite.

## Success Response (HTTP 200)
```json
{
  "id": 1,
  "message": "Article approved successfully",
  "status": "APPROVED"
}
```

## Error Responses
- **HTTP 404 Not Found**:
```json
{ "error": "Article not found" }
```
- **HTTP 400 Bad Request**:
```json
{ "error": "Only SUBMITTED articles can be approved" }
```
