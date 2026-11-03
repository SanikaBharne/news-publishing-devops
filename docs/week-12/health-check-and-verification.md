# Health Check and Verification

The application health response is defined by the existing Flask `/health` route. Jenkins first waits for Docker's health check and then calls the Windows-side health script:

```bat
python scripts\healthcheck.py 127.0.0.1 5001 20
powershell.exe -NoProfile -ExecutionPolicy Bypass -File scripts\verify_container.ps1 -ContainerName news-publishing-container
```

The Python script retries for up to about one minute and checks HTTP 200, `status: ok`, and the expected message. The PowerShell verifier requires the named container to be running and Docker health to be `healthy`, and confirms the container port is published. The deploy script performs the same health checks before it discards a previous deployment.

After Selenium tests, Final Verification checks the container state and health again, repeats the HTTP health request, and prints the exact image tag, container name, and URL.

On failure, deployment prints container logs and attempts rollback. Jenkins' failure handler also collects logs only when it can identify the named container as belonging to this project. Failure of the health helper, verifier, Selenium command, or Docker command fails the build.
