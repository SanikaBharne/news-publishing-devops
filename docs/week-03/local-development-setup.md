# Local Development Setup

## Prerequisites
- Python 3.x installed
- pip (Python package installer) installed
- Git installed

## Installation Steps

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```
This installs Flask and pytest along with their sub-dependencies (Jinja2, Werkzeug, etc.).

### 2. Verify Installation
```bash
python --version
pip --version
git --version
pip show flask
pip show pytest
```

### 3. Run the Application
```bash
python src/app.py
```
The Flask development server starts on `http://127.0.0.1:5000`.

### 4. Verify the Health Endpoint
Open a browser or use curl:
```bash
curl http://127.0.0.1:5000/health
```
Expected response:
```json
{"message":"News Publishing Workflow MVP running","status":"ok"}
```

### 5. Stop the Application
Press `Ctrl+C` in the terminal running the Flask server.

## Database Setup
SQLite requires no separate installation or configuration. The database file will be created automatically during feature development in Weeks 5-6. No database exists yet in the Week 3 skeleton.

## What Is NOT Set Up Yet
- No Jinja2 templates (planned Week 5-6)
- No SQLite database file (planned Week 5-6)
- No Jenkins (planned Week 7)
- No Docker (planned Week 11)
- No Selenium (planned Week 9)
- No Ansible (planned Week 13)
- No Gunicorn (planned Week 11)
