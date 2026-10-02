# Week 10 - Evidence Checklist

- [x] Jenkinsfile contains a dedicated Selenium testing stage.
- [x] Dependencies are installed in a Windows virtual environment.
- [x] Unit tests run before deployment.
- [x] Existing `scripts\deploy.py` starts Waitress on port 5001.
- [x] Existing health check gates Selenium execution.
- [x] Existing Selenium suite runs with `python -m pytest tests\selenium -v`.
- [x] Failed unit, health, or Selenium commands return a non-zero status to Jenkins.
- [x] Final health verification runs after Selenium.
- [x] Unit-test result recorded: 14 passed.
- [x] Selenium-test result recorded: 8 passed.
- [x] Branch and commit details recorded.

No screenshots are claimed or included by this documentation.
