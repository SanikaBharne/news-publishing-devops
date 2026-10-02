# Selenium Jenkins Integration

The Jenkinsfile runs the existing suite with:

```text
python -m pytest tests\selenium -v
```

The suite uses the existing `tests/selenium/conftest.py` fixture. It starts a headless Chrome WebDriver through Selenium Manager and targets `http://127.0.0.1:5001`. No new Selenium scenarios were added.

Jenkins runs the Selenium stage only after `scripts/healthcheck.py` confirms that the Waitress application is responding on the configured port.

The Jenkins agent must have Chrome available. Selenium Manager resolves a compatible ChromeDriver using the existing Selenium dependency.
