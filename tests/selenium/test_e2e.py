"""
test_e2e.py - Week 9: Selenium end-to-end tests for the News Publishing Workflow.

Prerequisites:
    The Flask application must be running on http://127.0.0.1:5001
    before executing this suite.  Start it with:
        python scripts/deploy.py

Run with:
    python -m pytest tests/selenium/ -v
"""

import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def wait_for_visible(driver, css, timeout=10):
    """Wait until an element matching *css* selector is visible and return it."""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, css))
    )


def wait_for_text_in_element(driver, css, text, timeout=10):
    """Wait until the element contains *text*."""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, css), text)
    )


def submit_article(driver, base_url, title, author, content):
    """Navigate to the submission page and submit an article."""
    driver.get(f"{base_url}/")
    wait_for_visible(driver, "#title")
    driver.find_element(By.ID, "title").clear()
    driver.find_element(By.ID, "title").send_keys(title)
    driver.find_element(By.ID, "author").clear()
    driver.find_element(By.ID, "author").send_keys(author)
    driver.find_element(By.ID, "content").clear()
    driver.find_element(By.ID, "content").send_keys(content)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # Wait for the message box to appear
    msg = wait_for_visible(driver, "#message")
    return msg


def open_article_in_reviewer(driver, base_url, title):
    """
    Navigate to the reviewer dashboard, find the row with *title*,
    click 'View / Review', and wait for the modal to open.
    Returns the modal element.
    """
    driver.get(f"{base_url}/reviewer")
    # Wait until at least one row with the article title is present
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#articles-table tbody"), title
        )
    )
    # Find rows and click the first one matching the title
    rows = driver.find_elements(By.CSS_SELECTOR, "#articles-table tbody tr")
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")
        if len(cells) >= 2 and cells[1].text == title:
            row.find_element(By.CSS_SELECTOR, ".btn-view").click()
            break

    modal = wait_for_visible(driver, "#article-modal")
    return modal


# ---------------------------------------------------------------------------
# Test scenarios
# ---------------------------------------------------------------------------

class TestArticleSubmission:
    """Scenarios 1-4: Submit a valid article and verify successful submission."""

    def test_submission_page_loads(self, driver, base_url):
        """Scenario 1: Open the article submission page."""
        driver.get(f"{base_url}/")
        assert "Submit" in driver.title or "Submit" in driver.page_source

    def test_valid_article_submission(self, driver, base_url):
        """Scenarios 2-4: Enter valid fields, submit, verify success message."""
        msg = submit_article(
            driver, base_url,
            title="Selenium Test Article",
            author="Test Author",
            content="This article was submitted by the Selenium E2E test suite."
        )
        assert msg.is_displayed(), "Success message should be visible after submission"
        assert "success" in msg.get_attribute("class"), \
            f"Message box should have 'success' class, got: {msg.get_attribute('class')}"
        assert "SUBMITTED" in msg.text or "Article ID" in msg.text, \
            f"Unexpected success message: {msg.text}"


class TestReviewerDashboard:
    """Scenarios 5-6: Reviewer dashboard shows submitted articles."""

    def test_reviewer_dashboard_loads(self, driver, base_url):
        """Scenario 5: Open the reviewer dashboard."""
        driver.get(f"{base_url}/reviewer")
        assert "Reviewer" in driver.title or "Reviewer" in driver.page_source

    def test_submitted_article_visible_in_dashboard(self, driver, base_url):
        """Scenario 6: The article submitted in the previous test is visible."""
        # Submit a fresh article so we know it will be there
        submit_article(
            driver, base_url,
            title="Dashboard Visibility Article",
            author="Reviewer Tester",
            content="Checking that the article appears in the reviewer dashboard."
        )
        driver.get(f"{base_url}/reviewer")
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#articles-table tbody"), "Dashboard Visibility Article"
            )
        )
        table_text = driver.find_element(By.ID, "articles-table").text
        assert "Dashboard Visibility Article" in table_text


class TestArticleApproval:
    """Scenarios 7-8: Approve an article and verify APPROVED status."""

    def test_approve_article(self, driver, base_url):
        """Scenarios 7-8: Open the modal, click Approve, verify APPROVED status in table."""
        title = "Article To Approve"
        submit_article(driver, base_url, title=title,
                       author="Approver", content="Content to be approved.")

        open_article_in_reviewer(driver, base_url, title)

        # Click the Approve button
        driver.find_element(By.CSS_SELECTOR, ".btn-approve").click()

        # The modal closes; success message should appear
        wait_for_visible(driver, "#message")
        msg_text = driver.find_element(By.ID, "message").text
        assert "approved" in msg_text.lower(), \
            f"Expected approval confirmation, got: {msg_text}"

        # The table should now show APPROVED for this article
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#articles-table tbody"), "APPROVED"
            )
        )
        table_text = driver.find_element(By.ID, "articles-table").text
        assert "APPROVED" in table_text


class TestArticleRejection:
    """Scenarios 9-11: Submit a second article, reject it with a comment, verify REJECTED."""

    def test_reject_article_with_comment(self, driver, base_url):
        """Scenarios 9-11: Submit article, reject with comment, verify REJECTED."""
        title = "Article To Reject"
        submit_article(driver, base_url, title=title,
                       author="Rejecter", content="Content to be rejected.")

        open_article_in_reviewer(driver, base_url, title)

        # Enter a rejection comment
        comment_box = driver.find_element(By.ID, "reject-comment")
        comment_box.clear()
        comment_box.send_keys("This article does not meet editorial standards.")

        # Click Reject
        driver.find_element(By.CSS_SELECTOR, ".btn-reject").click()

        # Confirm rejection message
        wait_for_visible(driver, "#message")
        msg_text = driver.find_element(By.ID, "message").text
        assert "rejected" in msg_text.lower(), \
            f"Expected rejection confirmation, got: {msg_text}"

        # Table should show REJECTED
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "#articles-table tbody"), "REJECTED"
            )
        )
        table_text = driver.find_element(By.ID, "articles-table").text
        assert "REJECTED" in table_text


class TestValidationErrors:
    """Scenarios 12-13: Required-field validation – empty fields rejected client-side."""

    def test_empty_submission_shows_error(self, driver, base_url):
        """
        Scenario 12-13: Submit with all fields empty.
        The browser enforces 'required' HTML attributes – the form should not
        submit and no success message should appear.
        """
        driver.get(f"{base_url}/")
        wait_for_visible(driver, "#title")

        # Do NOT fill in any fields; click Submit directly
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # The form has required attributes – HTML5 validation prevents submission.
        # The #message div should remain hidden (display:none).
        msg = driver.find_element(By.ID, "message")
        assert msg.value_of_css_property("display") == "none", \
            "Message box should stay hidden when required fields are empty"

    def test_whitespace_only_fields_show_error(self, driver, base_url):
        """
        Submit with whitespace-only values.
        The server rejects them with HTTP 400; the client shows an error box.
        """
        driver.get(f"{base_url}/")
        wait_for_visible(driver, "#title")
        driver.find_element(By.ID, "title").send_keys("   ")
        driver.find_element(By.ID, "author").send_keys("   ")
        driver.find_element(By.ID, "content").send_keys("   ")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        msg = wait_for_visible(driver, "#message")
        assert msg.is_displayed(), "Error message should be visible for whitespace-only fields"
        assert "error" in msg.get_attribute("class"), \
            f"Message box should have 'error' class, got: {msg.get_attribute('class')}"
        assert "required" in msg.text.lower() or "error" in msg.text.lower(), \
            f"Expected validation error text, got: {msg.text}"
