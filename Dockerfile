FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_PATH=/data/app.db

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd --create-home --shell /usr/sbin/nologin appuser \
    && mkdir /data \
    && chown appuser:appuser /data

COPY --chown=appuser:appuser src/ /app/src/

USER appuser

EXPOSE 5001

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:5001/health', timeout=3)"

CMD ["sh", "-c", "python -c 'from src.app import init_db; init_db()' && exec gunicorn --chdir src --bind 0.0.0.0:5001 --workers 2 --access-logfile - --error-logfile - app:app"]
