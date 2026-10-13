# SQLite Persistence

The existing app opens SQLite using the relative path `app.db`. That behavior is preserved for normal local use. A `DATABASE_PATH` environment-variable override now allows the container to store the database at `/data/app.db`.

Use a named Docker volume mounted at `/data`:

```powershell
docker volume create news-publishing-data
docker run -d --name news-publishing-container -p 5001:5001 -v news-publishing-data:/data -e DATABASE_PATH=/data/app.db news-publishing-app:week11
```

The Dockerfile creates `/data` and makes it writable by the non-root application user. The startup command calls the existing `init_db()` function, which creates tables only if missing; it does not delete database files or change the schema. Restarting or removing the container leaves the named volume intact.

The mounted volume behavior has not been exercised because Docker's Linux engine was unavailable. Preserve the volume when removing the container if its articles are needed.
