# Container Replacement and Safety

The deploy script manages only the exact configured container name after verifying the project label or the existing `news-publishing-app:*` image identity. It refuses to overwrite an unrecognized container, an unrelated container publishing port 5001, or an unexplained host listener. It never terminates a host process and never removes a Docker volume.

Deployment is repeatable:

1. Jenkins builds both image tags before deployment.
2. The new image is started as a uniquely named candidate using its disposable container filesystem for the database and must report Docker health `healthy`. This check does not mount or write to the persistent database volume.
3. The existing project container is stopped and renamed to a build-specific backup.
4. The new named container starts with the persistent SQLite volume and the published port.
5. Docker health and the external `/health` response are checked before the previous container is removed.

If deployment fails after replacement begins, the script prints logs for verified project containers, removes only the new labeled application container it started, and restores the previous container and running/stopped state when possible. The named database volume is retained.

The stable host port means replacement has a short service interruption: two containers cannot bind host port 5001 simultaneously. Image build and isolated health validation happen before that interruption. An unexpected Windows Waitress process on port 5001 causes a safe failure; stop that process through its normal owner/operator workflow before rerunning Jenkins. The old Week 8 broad `taskkill` loop is removed.
