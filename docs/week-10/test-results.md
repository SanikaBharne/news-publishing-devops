# Week 10 - Test Results

Verification on the Week 10 feature branch:

| Check | Result |
| --- | --- |
| Unit tests | 14 passed |
| Selenium tests | 8 passed |
| Application endpoint | Health check passed on port 5001 |

The unit stage targets only `tests/test_submission.py` and `tests/test_reviewer.py`. The Selenium stage separately targets `tests/selenium`, so browser tests are not run before the application is deployed.

For completeness, the requested broad command `python -m pytest -v` returned `14 passed, 8 errors` in this local Windows session because its combined Selenium discovery hit Selenium Manager's `WinError 6` invalid-handle setup error. The required Jenkins-equivalent commands were run separately and passed: 14 unit tests and 8 Selenium tests.

The test output includes existing `datetime.utcnow()` deprecation warnings from `src/app.py`; these do not fail the tests and are outside Week 10 scope.
