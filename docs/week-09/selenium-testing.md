# Week 9 – Selenium Testing

## Objective

The purpose of Selenium testing is to verify the application from the user's perspective rather than testing individual backend functions only.

The tests interact with the actual web interface and verify the resulting behavior.

## Testing Process

The Selenium testing workflow is:

```text
Start Application
       ↓
Open Browser
       ↓
Open Application
       ↓
Perform User Action
       ↓
Verify Expected Result
       ↓
Close Browser
```

## Test Environment

The tests were executed against:

```text
http://127.0.0.1:5001
```

The application was accessed through a headless Chrome browser.

## Selenium Result

The complete Selenium test suite produced:

```text
8 passed in 16.70s
```

All eight Selenium tests passed successfully.

## Existing Unit Tests

The existing unit test suite was also checked to ensure that Selenium changes did not affect the previous functionality.

Result:

```text
14 passed in 0.69s
```

The existing 14 tests remained unchanged and continued to pass.

## Week 9 Outcome

Both the new Selenium end-to-end tests and the existing unit tests passed successfully.