"""
deploy.py - Week 8: Deploy the Flask application on port 5001.

Gunicorn is the standard WSGI server for Flask in Linux/production environments.
On Windows (where Jenkins may run), gunicorn is not supported (missing fcntl).
This script uses 'waitress', the Windows-compatible production WSGI server,
as the deployment target for the local CI/CD pipeline.

Usage:
    python scripts/deploy.py
"""

import sys
import os

# Ensure the project root is on the path so 'src.app' can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import app, init_db

DEPLOY_PORT = 5001
DEPLOY_HOST = "127.0.0.1"

if __name__ == "__main__":
    # Initialise the database before serving
    with app.app_context():
        init_db()

    try:
        from waitress import serve
        print(f"Starting News Publishing Workflow on {DEPLOY_HOST}:{DEPLOY_PORT} (waitress WSGI server)")
        print(f"Health check: http://{DEPLOY_HOST}:{DEPLOY_PORT}/health")
        serve(app, host=DEPLOY_HOST, port=DEPLOY_PORT, threads=4)
    except ImportError:
        # Fallback: Flask development server (not for production)
        print("waitress not available – falling back to Flask dev server")
        app.run(host=DEPLOY_HOST, port=DEPLOY_PORT)
