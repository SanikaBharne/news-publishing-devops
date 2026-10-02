# Article Status Tracking Documentation

## Overview
Status tracking is implemented via the existing article retrieval endpoints (`GET /api/articles` and `GET /api/articles/<id>`). No redundant status tracking API was introduced, following clean REST principles.

## Allowed Article Statuses
1. `DRAFT`: Initial draft state (reserved for future editor expansion).
2. `SUBMITTED`: Default status assigned upon author submission via `POST /api/articles`.
3. `APPROVED`: Assigned upon successful reviewer approval via `PUT /api/articles/<id>/approve`.
4. `REJECTED`: Assigned upon reviewer rejection via `PUT /api/articles/<id>/reject`.

## Status Retrieval Endpoint
- **Method**: `GET`
- **Path**: `/api/articles/<id>`
- **Response (HTTP 200)**:
```json
{
  "id": 1,
  "title": "Tech Innovations 2026",
  "content": "Full article body...",
  "author": "Alice Doe",
  "status": "APPROVED",
  "comment": null,
  "submission_date": "2026-10-02 21:00:00",
  "review_date": "2026-10-02 21:30:00"
}
```

## Reviewer Dashboard Integration
The status field is dynamically rendered in the Reviewer Dashboard (`/reviewer`) and refreshed automatically after any review action.
