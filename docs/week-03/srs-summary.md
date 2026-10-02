# Software Requirements Specification (SRS) Summary

## Project Purpose
This project implements a CI/CD pipeline for a News Publishing Workflow as a 15-week academic DevOps project. The application is intentionally simple so that the primary focus remains on progressive DevOps implementation.

## Problem Summary
Manual news publishing workflows lack automated testing, continuous integration, and standardized configuration management. Deployments are slow, error-prone, and inconsistent across environments.

## MVP Scope
The application MVP contains ONLY:
1. News article/request submission
2. Required-field/data validation
3. Reviewer dashboard
4. Reviewer approval
5. Reviewer rejection with mandatory rejection comment
6. Article status tracking

## Actors
- **Writer / Journalist:** Submits news articles for review.
- **Reviewer / Editor:** Reviews, approves, or rejects submitted articles.

## Functional Requirements Summary
| ID | Requirement |
|---|---|
| FR-01 | Writer can submit a news article/request. |
| FR-02 | System validates required fields (title, content, author). |
| FR-03 | System provides validation feedback if fields are missing. |
| FR-04 | Reviewer can view a dashboard of submitted articles. |
| FR-05 | Reviewer can view full article details. |
| FR-06 | Reviewer can approve an article. |
| FR-07 | Reviewer can reject an article. |
| FR-08 | Rejection requires a mandatory rejection comment. |
| FR-09 | System updates article status immediately upon action. |
| FR-10 | Writer/Reviewer can view current article status. |

## Non-Functional Requirements Summary
- Usability, reliability, maintainability, testability, deployment consistency, portability, error handling, and logging.
- See `non-functional-requirements.md` for full details.

## Business and Workflow Rules

### Defined Statuses
- **SUBMITTED:** Article has been submitted by the Writer and awaits review.
- **APPROVED:** Reviewer has accepted the article.
- **REJECTED:** Reviewer has declined the article.

### Valid State Transitions
- *New Article* → **SUBMITTED**
- **SUBMITTED** → **APPROVED**
- **SUBMITTED** → **REJECTED**

### Rules
- A REJECTED action MUST contain a rejection comment.
- Roles are simulated via UI navigation; no authentication is required.
- Author is a plain text field entered by the writer; not linked to a user account.

## Constraints
- 15-week academic timeline.
- Monolithic architecture only; no microservices.
- Technology stack finalized in Week 3 (Python/Flask/SQLite).

## Assumptions
- A local development environment is available to run the application.
- Target deployment environment may be local or academically provided.
- Testing data will be synthetic and predefined.

## Out-of-Scope Items
- Authentication and RBAC
- Payment gateways or subscriptions
- AI news generation or recommendation systems
- Social media integrations, comments, or likes
- Real-time news feeds or complex UI animations
- Microservices or Kubernetes
- Analytics or notifications
