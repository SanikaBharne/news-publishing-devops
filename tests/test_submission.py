import pytest
import sqlite3
import os
import sys
import runpy

# Add the src directory to the path so app can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app, init_db

def test_database_path_environment_override(monkeypatch, tmp_path):
    configured_path = str(tmp_path / 'configured.db')
    monkeypatch.setenv('DATABASE_PATH', configured_path)

    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/app.py'))
    module_globals = runpy.run_path(app_path)

    assert module_globals['DATABASE'] == configured_path

@pytest.fixture
def client():
    # Configure app for testing
    app.config['TESTING'] = True
    
    # We will use an in-memory database or a separate test db
    # Since app.py hardcodes 'app.db', let's patch it for testing
    import app as myapp
    myapp.DATABASE = 'test_app.db'
    
    with app.app_context():
        # Initialize test DB
        init_db()
    
    with app.test_client() as client:
        yield client
        
    # Cleanup after tests
    if os.path.exists('test_app.db'):
        os.remove('test_app.db')

def test_valid_submission(client):
    response = client.post('/api/articles', json={
        "title": "Test Title",
        "content": "Test Content",
        "author": "Test Author"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Article submitted successfully"
    assert "id" in data
    assert data["status"] == "SUBMITTED"
    
def test_missing_title(client):
    response = client.post('/api/articles', json={
        "content": "Test Content",
        "author": "Test Author"
    })
    assert response.status_code == 400
    assert "required fields" in response.get_json()["error"]

def test_missing_content(client):
    response = client.post('/api/articles', json={
        "title": "Test Title",
        "author": "Test Author"
    })
    assert response.status_code == 400
    assert "required fields" in response.get_json()["error"]

def test_missing_author(client):
    response = client.post('/api/articles', json={
        "title": "Test Title",
        "content": "Test Content"
    })
    assert response.status_code == 400
    assert "required fields" in response.get_json()["error"]

def test_whitespace_only_fields(client):
    response = client.post('/api/articles', json={
        "title": "   ",
        "content": "Test Content",
        "author": "Test Author"
    })
    assert response.status_code == 400
    assert "required fields" in response.get_json()["error"]

def test_database_persistence_and_status(client):
    # Submit valid article
    client.post('/api/articles', json={
        "title": "Persistent Title",
        "content": "Persistent Content",
        "author": "Persistent Author"
    })
    
    # Verify in DB
    conn = sqlite3.connect('test_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, status FROM articles WHERE title='Persistent Title'")
    row = cursor.fetchone()
    conn.close()
    
    assert row is not None
    assert row[0] == "Persistent Title"
    assert row[1] == "SUBMITTED"
