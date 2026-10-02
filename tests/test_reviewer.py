import pytest
import sqlite3
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app, init_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    
    import app as myapp
    myapp.DATABASE = 'test_app_reviewer.db'
    
    with app.app_context():
        init_db()
    
    with app.test_client() as client:
        yield client
        
    if os.path.exists('test_app_reviewer.db'):
        os.remove('test_app_reviewer.db')

def submit_article(client):
    response = client.post('/api/articles', json={
        "title": "Review Title",
        "content": "Review Content",
        "author": "Review Author"
    })
    return response.get_json()["id"]

def test_reviewer_dashboard_listing(client):
    article_id = submit_article(client)
    response = client.get('/api/articles')
    assert response.status_code == 200
    articles = response.get_json()
    assert len(articles) > 0
    assert any(a["id"] == article_id for a in articles)

def test_approve_valid_submitted_article(client):
    article_id = submit_article(client)
    response = client.put(f'/api/articles/{article_id}/approve')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "APPROVED"
    assert data["message"] == "Article approved successfully"

def test_verify_approval_status(client):
    article_id = submit_article(client)
    client.put(f'/api/articles/{article_id}/approve')
    
    # Status tracking through article GET
    response = client.get(f'/api/articles/{article_id}')
    assert response.status_code == 200
    assert response.get_json()["status"] == "APPROVED"

def test_reject_valid_submitted_article(client):
    article_id = submit_article(client)
    response = client.put(f'/api/articles/{article_id}/reject', json={
        "comment": "Needs factual corrections."
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "REJECTED"
    assert data["message"] == "Article rejected successfully"

def test_verify_rejection_status_and_comment(client):
    article_id = submit_article(client)
    client.put(f'/api/articles/{article_id}/reject', json={
        "comment": "Inappropriate content."
    })
    
    response = client.get(f'/api/articles/{article_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "REJECTED"
    assert data["comment"] == "Inappropriate content."

def test_reject_without_comment(client):
    article_id = submit_article(client)
    response = client.put(f'/api/articles/{article_id}/reject', json={})
    assert response.status_code == 400
    assert "mandatory" in response.get_json()["error"].lower()

def test_reject_with_whitespace_comment(client):
    article_id = submit_article(client)
    response = client.put(f'/api/articles/{article_id}/reject', json={
        "comment": "   "
    })
    assert response.status_code == 400
    assert "mandatory" in response.get_json()["error"].lower()

def test_invalid_article_id(client):
    response = client.put('/api/articles/999/approve')
    assert response.status_code == 404
    assert response.get_json()["error"] == "Article not found"
    
    response = client.put('/api/articles/999/reject', json={"comment": "No"})
    assert response.status_code == 404
    
    response = client.get('/api/articles/999')
    assert response.status_code == 404
