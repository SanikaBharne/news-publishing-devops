"""
conftest.py for Selenium tests.

Provides a module-scoped Chrome WebDriver fixture that points at the
application configured by APP_BASE_URL, or the local port 5001 default.
The app must be running before these tests are executed.
"""
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = os.environ.get("APP_BASE_URL", "http://127.0.0.1:5001").rstrip("/")


def pytest_configure(config):
    """Register the selenium marker so pytest does not warn about unknown marks."""
    config.addinivalue_line(
        "markers",
        "selenium: marks tests as Selenium end-to-end tests (requires running app on port 5001)"
    )


@pytest.fixture(scope="module")
def driver():
    """
    Headless Chrome WebDriver for Selenium tests.
    Uses Selenium Manager (Selenium ≥ 4.6) to automatically download
    a matching ChromeDriver – no manual driver installation required.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(10)  # seconds – used for element lookups
    yield drv
    drv.quit()


@pytest.fixture(scope="module")
def base_url():
    return BASE_URL
