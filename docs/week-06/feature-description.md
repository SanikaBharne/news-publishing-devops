# Week 6 Feature Description – Reviewer Workflow & MVP Completion

## Overview
Week 6 completes the core Minimum Viable Product (MVP) for the **CI/CD Pipeline for a News Publishing Workflow** academic project. While Week 5 implemented the author's submission interface and endpoint (`POST /api/articles`), Week 6 implements the reviewer's workflow for inspecting, approving, or rejecting submitted news articles.

## Business Context & Value
In a professional publishing workflow, content created by authors must undergo editorial review before publication. This feature provides:
- Centralized visibility into all submitted articles.
- Editorial decision controls (**Approve** / **Reject**).
- Mandatory auditability for rejected content (requiring explicit rejection feedback).
- Complete lifecycle tracking (`SUBMITTED` → `APPROVED` / `REJECTED`).

## Scope & Boundaries
- **In-Scope**:
  - Reviewer dashboard UI (`/reviewer`) displaying all submitted articles.
  - Article approval endpoint (`PUT /api/articles/<id>/approve`).
  - Article rejection endpoint (`PUT /api/articles/<id>/reject`) with mandatory non-whitespace comment validation.
  - Single article detail & status endpoint (`GET /api/articles/<id>`).
  - Automated unit test suite using `pytest`.
- **Out-of-Scope (Strictly Enforced)**:
  - Authentication / RBAC / User accounts.
  - Category tagging, media uploads, or AI tools.
  - Jenkins, Docker, Selenium, Ansible, production deployments (reserved for Weeks 7–15).
