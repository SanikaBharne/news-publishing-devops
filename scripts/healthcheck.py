"""
healthcheck.py - Week 8: Automated health check for the deployed application.

Polls the /health endpoint of the deployed Flask app.
Exits with code 0 on success, code 1 on failure (causing Jenkins to fail the stage).

Usage:
    python scripts/healthcheck.py [host] [port] [retries]
"""

import sys
import time
import urllib.request
import urllib.error
import json

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 5001
RETRIES = int(sys.argv[3]) if len(sys.argv) > 3 else 10
DELAY = 3  # seconds between retries

url = f"http://{HOST}:{PORT}/health"
print(f"Health check target: {url}")

for attempt in range(1, RETRIES + 1):
    try:
        response = urllib.request.urlopen(url, timeout=5)
        body = response.read().decode("utf-8")
        data = json.loads(body)
        if response.status == 200 and data.get("status") == "ok":
            print(f"[PASS] Health check passed (attempt {attempt}): {body}")
            sys.exit(0)
        else:
            print(f"[WARN] Unexpected response (attempt {attempt}): HTTP {response.status} {body}")
    except (urllib.error.URLError, OSError) as e:
        print(f"[WAIT] Attempt {attempt}/{RETRIES}: {e}")

    if attempt < RETRIES:
        time.sleep(DELAY)

print("[FAIL] Health check failed after all retries. Pipeline will fail.")
sys.exit(1)
