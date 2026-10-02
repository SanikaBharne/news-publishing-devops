# Week 10 - Test Execution

Install dependencies locally:

```text
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Run the unit tests:

```text
python -m pytest tests\test_submission.py tests\test_reviewer.py -v
```

Start the existing Week 8 deployment in another terminal:

```text
python scripts\deploy.py
```

Run the Selenium tests:

```text
python -m pytest tests\selenium -v
```

The broad `python -m pytest -v` command discovers both unit and Selenium tests because pytest searches the whole `tests` tree. In local verification it produced 14 passed unit tests and 8 Selenium setup errors from Selenium Manager's Windows process handle (`WinError 6`). The Jenkins pipeline therefore keeps unit and browser execution in separate stages; the dedicated Selenium command passed all 8 tests.

Check the running application directly when needed:

```text
python scripts\healthcheck.py 127.0.0.1 5001 10
```

The Jenkinsfile uses the same commands with the virtual environment activated through `call venv\Scripts\activate.bat`.
