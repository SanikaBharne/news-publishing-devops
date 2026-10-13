import os
import sys

import pytest
from werkzeug.security import generate_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import app as app_module
from app import app, init_db


@pytest.fixture
def client(tmp_path):
    app.config.update(TESTING=True)
    app_module.DATABASE = str(tmp_path / "newsflow-test.db")
    with app.app_context():
        init_db()
        db = app_module.get_db()
        reader = db.execute(
            "INSERT INTO users (username, password_hash, role, display_name) VALUES (?, ?, ?, ?)",
            ("reader", generate_password_hash("reader-pass"), "reader", "Reader One"),
        ).lastrowid
        publisher = db.execute(
            "INSERT INTO users (username, password_hash, role, display_name) VALUES (?, ?, ?, ?)",
            ("publisher", generate_password_hash("publisher-pass"), "publisher", "Publisher One"),
        ).lastrowid
        approved = db.execute(
            """INSERT INTO articles (title, content, author, status, category, summary, user_id)
               VALUES ('Public story', 'Approved content', 'Reporter', 'APPROVED', 'Local', 'A summary', ?)""",
            (publisher,),
        ).lastrowid
        pending = db.execute(
            """INSERT INTO articles (title, content, author, status, category, user_id)
               VALUES ('Private story', 'Pending content', 'Reporter', 'SUBMITTED', 'Local', ?)""",
            (publisher,),
        ).lastrowid
        db.commit()
    with app.test_client() as test_client:
        yield test_client, reader, publisher, approved, pending


def _set_identity(client, user_id):
    with client.session_transaction() as session:
        session["user_id"] = user_id
        session["_csrf_token"] = "csrf-test"


def test_login_uses_hashed_password_and_distinct_roles(client):
    test_client, reader_id, _, _, _ = client
    page = test_client.get("/reader/login")
    assert page.status_code == 200
    with test_client.session_transaction() as session:
        token = session["_csrf_token"]
    response = test_client.post(
        "/reader/login",
        data={"username": "reader", "password": "reader-pass", "_csrf_token": token},
    )
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/reader")
    with test_client.session_transaction() as session:
        assert session["user_id"] == reader_id
    assert test_client.get("/publisher").status_code == 403


def test_reader_only_sees_approved_articles_and_private_routes_are_blocked(client):
    test_client, reader_id, _, approved_id, pending_id = client
    _set_identity(test_client, reader_id)
    response = test_client.get("/api/public/articles")
    assert response.status_code == 200
    assert [article["title"] for article in response.get_json()] == ["Public story"]
    assert test_client.get(f"/article/{approved_id}").status_code == 200
    assert test_client.get(f"/article/{pending_id}").status_code == 404
    assert test_client.get(f"/api/public/articles/{pending_id}").status_code == 404
    assert test_client.get("/api/articles").status_code == 403
    assert test_client.put(
        f"/api/articles/{pending_id}/approve", headers={"X-CSRF-Token": "csrf-test"}
    ).status_code == 403


def test_public_search_and_category_filter_only_search_approved(client):
    test_client, _, _, _, _ = client
    assert len(test_client.get("/api/public/articles?q=Public&category=Local").get_json()) == 1
    assert test_client.get("/api/public/articles?q=Private").get_json() == []
    assert test_client.get("/api/public/articles?category=Culture").get_json() == []


def test_reader_can_bookmark_only_approved_articles(client):
    test_client, reader_id, _, approved_id, pending_id = client
    _set_identity(test_client, reader_id)
    saved = test_client.post(
        "/api/reader/bookmarks",
        json={"article_id": approved_id},
        headers={"X-CSRF-Token": "csrf-test"},
    )
    assert saved.status_code == 201
    assert [item["id"] for item in test_client.get("/api/reader/bookmarks").get_json()] == [approved_id]
    assert test_client.post(
        "/api/reader/bookmarks",
        json={"article_id": pending_id},
        headers={"X-CSRF-Token": "csrf-test"},
    ).status_code == 404
    assert test_client.delete(
        f"/api/reader/bookmarks/{approved_id}", headers={"X-CSRF-Token": "csrf-test"}
    ).status_code == 200
    assert test_client.get("/api/reader/bookmarks").get_json() == []


def test_publisher_can_save_draft_then_submit_and_cannot_self_review(client):
    test_client, _, publisher_id, _, _ = client
    _set_identity(test_client, publisher_id)
    response = test_client.post(
        "/publisher/articles/new",
        data={
            "_csrf_token": "csrf-test",
            "title": "Draft headline",
            "content": "Draft story",
            "category": "Culture",
            "action": "draft",
        },
    )
    assert response.status_code == 302
    db = app_module.sqlite3.connect(app_module.DATABASE)
    row = db.execute("SELECT id, status, category, user_id FROM articles WHERE title='Draft headline'").fetchone()
    db.close()
    assert row[1:] == ("DRAFT", "Culture", publisher_id)
    assert test_client.get(f"/article/{row[0]}").status_code == 404
    assert test_client.put(
        f"/api/articles/{row[0]}/approve", headers={"X-CSRF-Token": "csrf-test"}
    ).status_code == 400

    submitted = test_client.post(
        "/api/articles",
        json={"title": "Own submission", "content": "Story", "author": "Publisher One"},
        headers={"X-CSRF-Token": "csrf-test"},
    )
    assert submitted.status_code == 201
    assert test_client.put(
        f"/api/articles/{submitted.get_json()['id']}/approve",
        headers={"X-CSRF-Token": "csrf-test"},
    ).status_code == 403


def test_state_changes_require_csrf(client):
    test_client, _, publisher_id, _, pending_id = client
    _set_identity(test_client, publisher_id)
    response = test_client.put(f"/api/articles/{pending_id}/approve")
    assert response.status_code == 400
    assert "verified" in response.get_json()["error"]
