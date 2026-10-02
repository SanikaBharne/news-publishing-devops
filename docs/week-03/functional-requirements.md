# Functional Requirements

| ID | Requirement | Actor | Priority | Acceptance / Completion Condition |
|---|---|---|---|---|
| FR-01 | Writer can submit a news article/request. | Writer | High | Article is saved with status SUBMITTED and confirmation is displayed. |
| FR-02 | System validates required fields (title, content, author). | System | High | Submission is blocked if any required field is empty. |
| FR-03 | System provides validation feedback if fields are missing. | System | High | A clear error message is displayed identifying the missing field(s). |
| FR-04 | Reviewer can view a dashboard of submitted articles. | Reviewer | High | Pending articles are listed with title, author, and submission date. |
| FR-05 | Reviewer can view full article details. | Reviewer | High | Full title, content, author, date, and status are displayed. |
| FR-06 | Reviewer can approve an article. | Reviewer | High | Article status changes to APPROVED. |
| FR-07 | Reviewer can reject an article. | Reviewer | High | Article status changes to REJECTED with a comment attached. |
| FR-08 | Rejection requires a mandatory rejection comment. | System | High | System blocks rejection if the comment field is empty. |
| FR-09 | System updates article status immediately upon action. | System | High | Status changes are reflected in the dashboard immediately. |
| FR-10 | Writer/Reviewer can view current article status. | Writer/Reviewer | High | Current status (SUBMITTED, APPROVED, REJECTED) is visible in the article list and details. |
