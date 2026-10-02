# Reviewer Dashboard Documentation

## Overview
The Reviewer Dashboard provides a web interface accessible at `/reviewer` for editorial staff to inspect submitted articles and perform review actions.

## User Interface Elements
1. **Article Table**:
   - **ID**: Unique primary key of the article.
   - **Title**: Article headline.
   - **Author**: Submitting author's name.
   - **Submission Date**: UTC timestamp when article was submitted.
   - **Status**: Current status (`SUBMITTED`, `APPROVED`, `REJECTED`).
   - **Actions**: "View / Review" button for each article.

2. **Article Review Modal**:
   - Displays full title, author, submission date, status, and article content.
   - For `SUBMITTED` articles:
     - **Approve Button**: Triggers `PUT /api/articles/<id>/approve`.
     - **Rejection Input**: Text field for mandatory rejection comment.
     - **Reject Button**: Triggers `PUT /api/articles/<id>/reject`.
   - For `APPROVED` or `REJECTED` articles:
     - Action buttons are hidden to prevent status tampering.

## Technical Implementation
- Template: `src/templates/reviewer.html`
- Route: `GET /reviewer` in `src/app.py`
- Frontend fetch calls `GET /api/articles` to populate table dynamically on page load.
