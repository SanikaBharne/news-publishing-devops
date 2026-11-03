# Testing and Verification

## Unit tests

Run only the existing unit test modules (this does not collect Selenium tests):

```powershell
python -m pytest tests\test_submission.py tests\test_reviewer.py -v
```

**Executed result:** 15 tests passed in 1.20 seconds, including the new environment database-path test. Pytest reported existing `datetime.utcnow()` deprecation warnings from `src/app.py`; these warnings did not fail tests.

## Application health

**Executed result:** a local Flask test-client request to `/health` returned HTTP 200 and the expected `status: ok` JSON. The root health route was verified without starting a separate server.

## Docker verification

`docker --version` succeeded. `docker info` failed because Docker Desktop's Linux engine pipe was not available. Therefore the image build, container startup, network port access, Docker health state, container log inspection, container SQLite workflow, and stop/start/restart/removal lifecycle were not run or verified. Run the commands in the other Week 11 guides after starting Docker Desktop.

Host port 5001 was checked and no listening socket was found at verification time. No container or image was created or removed.
