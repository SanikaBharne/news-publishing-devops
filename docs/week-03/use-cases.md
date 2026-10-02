# Use Cases

## Actors
- **Writer / Journalist**: Submits news articles for review.
- **Reviewer / Editor**: Reviews, approves, or rejects articles.

---

### UC-01: Submit Article
- **ID:** UC-01
- **Name:** Submit Article
- **Actor:** Writer
- **Goal:** Submit a new news article for review.
- **Preconditions:** Writer accesses the submission page.
- **Main Flow:**
  1. Writer navigates to the submission form.
  2. Writer enters title, content, and author name.
  3. Writer clicks "Submit".
  4. System validates required fields.
  5. System saves the article with status SUBMITTED and current timestamp.
  6. System displays a confirmation message.
- **Alternative Flow:** None.
- **Exception Flow:** If any required field is empty, system displays a validation error and does not save. Writer corrects and resubmits.
- **Postconditions:** A new article exists in the database with status SUBMITTED.

---

### UC-02: View Submission Status
- **ID:** UC-02
- **Name:** View Submission Status
- **Actor:** Writer, Reviewer
- **Goal:** View the current status of submitted articles.
- **Preconditions:** At least one article exists in the system.
- **Main Flow:**
  1. User navigates to the articles list.
  2. System displays all articles with their current status (SUBMITTED, APPROVED, REJECTED).
- **Alternative Flow:** If no articles exist, system displays an empty list or a message.
- **Exception Flow:** None.
- **Postconditions:** User is informed of article statuses.

---

### UC-03: View Article Details
- **ID:** UC-03
- **Name:** View Article Details
- **Actor:** Reviewer
- **Goal:** Read the full content of a submitted article.
- **Preconditions:** An article exists in the system.
- **Main Flow:**
  1. Reviewer views the article list.
  2. Reviewer clicks on an article to view details.
  3. System displays the full title, content, author, submission date, and status.
- **Alternative Flow:** None.
- **Exception Flow:** If the article does not exist, system returns a "not found" message.
- **Postconditions:** Reviewer has read the article content.

---

### UC-04: Approve Article
- **ID:** UC-04
- **Name:** Approve Article
- **Actor:** Reviewer
- **Goal:** Approve a submitted article.
- **Preconditions:** An article exists with status SUBMITTED. Reviewer is viewing the article details.
- **Main Flow:**
  1. Reviewer clicks "Approve".
  2. System changes the article status to APPROVED.
  3. System displays a confirmation message.
- **Alternative Flow:** None.
- **Exception Flow:** If the article is not in SUBMITTED status, system rejects the action.
- **Postconditions:** Article status is APPROVED. Article no longer appears in the pending review queue.

---

### UC-05: Reject Article
- **ID:** UC-05
- **Name:** Reject Article
- **Actor:** Reviewer
- **Goal:** Reject a submitted article with a mandatory reason.
- **Preconditions:** An article exists with status SUBMITTED. Reviewer is viewing the article details.
- **Main Flow:**
  1. Reviewer clicks "Reject".
  2. System prompts for a rejection comment.
  3. Reviewer enters a comment.
  4. System changes the article status to REJECTED and stores the comment.
  5. System displays a confirmation message.
- **Alternative Flow:** None.
- **Exception Flow:** If the rejection comment is empty, system blocks the rejection and prompts the reviewer to enter a comment.
- **Postconditions:** Article status is REJECTED with the rejection comment stored.
