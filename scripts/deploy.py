"""
deploy.py - Start the Flask application on port 5001 using waitress.
Used by Jenkins Deploy stage and for local Selenium testing.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import app, init_db

DEPLOY_PORT = 5001
DEPLOY_HOST = "127.0.0.1"

if __name__ == "__main__":
    with app.app_context():
        init_db()

    try:
        from waitress import serve
        print(f"Starting News Publishing Workflow on {DEPLOY_HOST}:{DEPLOY_PORT} (waitress)")
        serve(app, host=DEPLOY_HOST, port=DEPLOY_PORT, threads=4)
    except ImportError:
        print("waitress not found – using Flask dev server")
        app.run(host=DEPLOY_HOST, port=DEPLOY_PORT)
