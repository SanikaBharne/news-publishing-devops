# Week 9 – Selenium Setup

## Objective

The objective of Week 9 was to introduce Selenium-based end-to-end testing for the News Publishing Workflow application.

Selenium is used to simulate real user interactions with the application through a web browser.

## Selenium Configuration

Selenium was added to the project dependencies through `requirements.txt`.

A dedicated Selenium test directory was created:

```text
tests/selenium/
```

The directory contains:

* `conftest.py`
* `test_e2e.py`

## Browser Configuration

A headless Chrome WebDriver fixture was created in:

```text
tests/selenium/conftest.py
```

The headless configuration allows Selenium tests to run without opening a visible browser window.

Selenium Manager is used to manage the browser driver.

## Application Under Test

The Selenium tests run against the locally deployed application on:

```text
http://127.0.0.1:5001
```

This is the same deployment environment introduced during Week 8.

## Week 9 Outcome

Selenium was successfully configured and used for automated end-to-end testing of the application's main user workflows.