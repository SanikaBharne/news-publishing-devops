"""
Isolated Flask application and Chrome fixtures for the Selenium suite.

The suite uses a temporary SQLite database and ephemeral test-only accounts;
it never writes to the developer's persistent app.db or deployed container.
"""
import os
import socket
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


ROOT = Path(__file__).resolve().parents[2]
TEST_PUBLISHER = "selenium-author"
TEST_REVIEWER = "selenium-reviewer"
TEST_PASSWORD = "temporary-selenium-password"


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "selenium: marks tests as isolated Selenium end-to-end tests",
    )


@pytest.fixture(scope="module")
def app_server():
    with tempfile.TemporaryDirectory(prefix="newsflow-selenium-") as data_dir:
        with socket.socket() as sock:
            sock.bind(("127.0.0.1", 0))
            port = sock.getsockname()[1]
        env = os.environ.copy()
        env.update(
            {
                "APP_PORT": str(port),
                "DATABASE_PATH": str(Path(data_dir) / "selenium.db"),
                "SECRET_KEY": "ephemeral-selenium-only-key",
                "DEMO_PUBLISHER_USERNAME": TEST_PUBLISHER,
                "DEMO_PUBLISHER_PASSWORD": TEST_PASSWORD,
                "DEMO_REVIEWER_USERNAME": TEST_REVIEWER,
                "DEMO_REVIEWER_PASSWORD": TEST_PASSWORD,
                "DEMO_READER_USERNAME": "selenium-reader",
                "DEMO_READER_PASSWORD": TEST_PASSWORD,
            }
        )
        process = subprocess.Popen(
            [sys.executable, str(ROOT / "scripts" / "deploy.py")],
            cwd=str(ROOT),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        base_url = f"http://127.0.0.1:{port}"
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            if process.poll() is not None:
                output = process.stdout.read() if process.stdout else ""
                raise RuntimeError(f"Test server exited before startup:\n{output}")
            try:
                with urllib.request.urlopen(f"{base_url}/health", timeout=1) as response:
                    if response.status == 200:
                        break
            except (urllib.error.URLError, TimeoutError, OSError):
                time.sleep(0.25)
        else:
            process.terminate()
            process.wait(timeout=5)
            output = process.stdout.read() if process.stdout else ""
            raise RuntimeError(f"Test server did not become healthy:\n{output}")
        os.environ["NEWSFLOW_TEST_PUBLISHER_USERNAME"] = TEST_PUBLISHER
        os.environ["NEWSFLOW_TEST_REVIEWER_USERNAME"] = TEST_REVIEWER
        os.environ["NEWSFLOW_TEST_READER_USERNAME"] = "selenium-reader"
        os.environ["NEWSFLOW_TEST_PASSWORD"] = TEST_PASSWORD
        try:
            yield base_url
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


@pytest.fixture(scope="module")
def driver(app_server):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,900")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture(scope="module")
def base_url(app_server):
    return app_server
