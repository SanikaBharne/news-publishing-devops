# API Specification

*Note: This is the API design for the MVP. These endpoints will be implemented during Weeks 5-6 (Feature Development). Only the `/health` endpoint currently exists.*

## Endpoints

| Method | Endpoint | Purpose | Request Body | Response Body | Status Code |
|---|---|---|---|---|---|
| `GET` | `/health` | Health check (verify app is running). | None | `{"status":"ok","message":"News Publishing Workflow MVP running"}` | `200 OK` |
| `POST` | `/api/articles` | Submit a new article. | `{"title":"...","content":"...","author":"..."}` | `{"message":"Article submitted","id":1}` | `201 Created` |
| `GET` | `/api/articles` | Retrieve all articles (dashboard + status tracking). | None | `[{"id":1,"title":"...","status":"SUBMITTED",...}]` | `200 OK` |
| `GET` | `/api/articles/<id>` | Retrieve full details of a specific article. | None | `{"id":1,"title":"...","content":"...","status":"..."}` | `200 OK` |
| `PUT` | `/api/articles/<id>/approve` | Approve a submitted article. | None | `{"message":"Article approved"}` | `200 OK` |
| `PUT` | `/api/articles/<id>/reject` | Reject a submitted article (mandatory comment). | `{"comment":"Rejection reason..."}` | `{"message":"Article rejected"}` | `200 OK` |

## Error Responses

| Condition | Status Code | Response |
|---|---|---|
| Required field missing on submit | `400 Bad Request` | `{"error":"Title is required"}` |
| Article not found | `404 Not Found` | `{"error":"Article not found"}` |
| Rejection without comment | `400 Bad Request` | `{"error":"Rejection comment is required"}` |

## Implementation Status

| Endpoint | Status |
|---|---|
| `GET /health` | **Implemented** (Week 3 skeleton) |
| `POST /api/articles` | Planned (Week 5) |
| `GET /api/articles` | Planned (Week 5) |
| `GET /api/articles/<id>` | Planned (Week 5) |
| `PUT /api/articles/<id>/approve` | Planned (Week 6) |
| `PUT /api/articles/<id>/reject` | Planned (Week 6) |

*Note: A separate `/status` endpoint is not needed because `GET /api/articles/<id>` already returns the article status.*
