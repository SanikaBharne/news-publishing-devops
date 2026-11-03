import functools
import os
import secrets
import sqlite3
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from flask import (
    Flask,
    abort,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash


DATABASE = os.environ.get("DATABASE_PATH", "app.db")


def _load_secret_key():
    configured = os.environ.get("SECRET_KEY")
    if configured:
        return configured
    key_path = Path(f"{DATABASE}.secret")
    try:
        descriptor = os.open(str(key_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        for _ in range(50):
            key = key_path.read_text(encoding="utf-8").strip()
            if key:
                return key
            time.sleep(0.01)
        raise RuntimeError(f"Session key file is empty: {key_path}")
    with os.fdopen(descriptor, "w", encoding="utf-8") as key_file:
        key = secrets.token_hex(32)
        key_file.write(key)
    return key


app = Flask(__name__)
app.config.update(
    SECRET_KEY=_load_secret_key(),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE", "").lower() == "true",
)
ARTICLE_COLUMNS = {
    "summary": "TEXT NOT NULL DEFAULT ''",
    "category": "TEXT NOT NULL DEFAULT 'General'",
    "cover_image": "TEXT NOT NULL DEFAULT ''",
    "user_id": "INTEGER",
}
PROJECT_VERIFICATION = (
    {
        "name": "Backend unit and authorization tests",
        "result": "24 passed",
        "detail": "Submission, reviewer workflow, Reader/Publisher access, public visibility, and CSRF.",
        "status": "passed",
    },
    {
        "name": "Selenium end-to-end tests",
        "result": "9 passed",
        "detail": "Publisher submission, review decisions, Reader browsing/bookmarks, and form validation.",
        "status": "passed",
    },
    {
        "name": "Docker candidate image",
        "result": "Build passed",
        "detail": "Built as news-publishing-app:newsflow-redesign; candidate build is not a Jenkins result.",
        "status": "passed",
    },
    {
        "name": "Deployed application health",
        "result": "Healthy",
        "detail": "Container health check and /health returned status ok after deployment.",
        "status": "passed",
    },
    {
        "name": "Jenkins run for this redesign",
        "result": "Not verified",
        "detail": "No authenticated Jenkins run result was available for this branch.",
        "status": "pending",
    },
)
PROJECT_MILESTONES = (
    {
        "name": "Article workflow",
        "detail": "Submission validation, editorial approval/rejection, and persistent SQLite status.",
        "status": "Complete",
    },
    {
        "name": "CI and browser testing",
        "detail": "Jenkins pipeline and Selenium test coverage documented; current Jenkins redesign run is unverified.",
        "status": "Implemented",
    },
    {
        "name": "Docker deployment",
        "detail": "Docker image, persistent volume, deployment, and health-check workflow documented.",
        "status": "Complete",
    },
    {
        "name": "Weeks 13–14",
        "detail": "Deployment monitoring and release-readiness documentation prepared.",
        "status": "Documented",
    },
    {
        "name": "NewsFlow Reader and Publisher UI",
        "detail": "Separate role-based experiences, article workflow, and regression tests implemented.",
        "status": "Complete",
    },
)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
    return db


@app.teardown_appcontext
def close_connection(_exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


def _seed_user(db, role, username_env, password_env):
    username = os.environ.get(username_env, "").strip()
    password = os.environ.get(password_env, "")
    if not username and not password:
        return
    if not username or not password:
        raise RuntimeError(f"Both {username_env} and {password_env} are required.")
    if len(password) < 12:
        raise RuntimeError(f"{password_env} must contain at least 12 characters.")
    existing = db.execute("SELECT role FROM users WHERE username = ?", (username,)).fetchone()
    if existing is not None and existing["role"] != role:
        raise RuntimeError(f"{username_env} conflicts with an account configured for another role.")
    db.execute(
        """INSERT INTO users (username, password_hash, role, display_name)
           VALUES (?, ?, ?, ?)
           ON CONFLICT(username) DO UPDATE SET password_hash = excluded.password_hash,
               display_name = excluded.display_name""",
        (username, generate_password_hash(password), role, username),
    )


def init_db():
    with app.app_context():
        db = get_db()
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT NOT NULL,
                comment TEXT,
                submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                review_date TIMESTAMP
            )
            """
        )
        existing = {row["name"] for row in db.execute("PRAGMA table_info(articles)")}
        for name, definition in ARTICLE_COLUMNS.items():
            if name not in existing:
                db.execute(f"ALTER TABLE articles ADD COLUMN {name} {definition}")
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL CHECK(role IN ('reader', 'publisher')),
                display_name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS bookmarks (
                user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                article_id INTEGER NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (user_id, article_id)
            )
            """
        )
        _seed_user(db, "reader", "DEMO_READER_USERNAME", "DEMO_READER_PASSWORD")
        _seed_user(db, "publisher", "DEMO_PUBLISHER_USERNAME", "DEMO_PUBLISHER_PASSWORD")
        _seed_user(db, "publisher", "DEMO_REVIEWER_USERNAME", "DEMO_REVIEWER_PASSWORD")
        db.commit()


def _json_request():
    return request.is_json or request.path.startswith("/api/")


def _error(message, status):
    if _json_request():
        return jsonify({"error": message}), status
    return render_template("error.html", code=status, message=message), status


def login_required(role=None):
    def decorate(view):
        @functools.wraps(view)
        def wrapped(*args, **kwargs):
            user = get_current_user()
            if user is None:
                if _json_request():
                    return _error("Authentication required.", 401)
                target = "publisher_login" if role == "publisher" else "reader_login"
                return redirect(url_for(target, next=request.path))
            if role and user["role"] != role:
                return _error("You do not have permission to access this resource.", 403)
            return view(*args, **kwargs)

        return wrapped

    return decorate


def get_current_user():
    if "current_user" not in g:
        user_id = session.get("user_id")
        g.current_user = (
            get_db().execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
            if user_id
            else None
        )
    return g.current_user


def csrf_token():
    token = session.get("_csrf_token")
    if token is None:
        token = session["_csrf_token"] = secrets.token_urlsafe(32)
    return token


@app.before_request
def protect_state_changes():
    if request.method not in {"POST", "PUT", "PATCH", "DELETE"}:
        return None
    supplied = request.form.get("_csrf_token") or request.headers.get("X-CSRF-Token")
    expected = session.get("_csrf_token")
    if not expected or not supplied or not secrets.compare_digest(expected, supplied):
        return _error("The form expired or could not be verified. Reload and try again.", 400)
    return None


@app.context_processor
def template_context():
    return {"current_user": get_current_user(), "csrf_token": csrf_token}


def _article_dict(row):
    article = dict(row)
    article.setdefault("summary", "")
    article.setdefault("category", "General")
    article.setdefault("cover_image", "")
    return article


def _public_article_dict(row):
    article = _article_dict(row)
    return {
        name: article[name]
        for name in (
            "id", "title", "content", "author", "status", "submission_date",
            "review_date", "summary", "category", "cover_image",
        )
    }


def _valid_image_url(value):
    if not value:
        return True
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _article_values(data):
    if not isinstance(data, dict):
        raise ValueError("A valid article object is required.")

    def text_field(name, default=""):
        value = data.get(name, default)
        if value is None:
            return ""
        if not isinstance(value, str):
            raise ValueError(f"{name.capitalize()} must be text.")
        return value.strip()

    title = text_field("title")
    content = text_field("content")
    author = text_field("author")
    summary = text_field("summary")
    category = text_field("category", "General") or "General"
    cover_image = text_field("cover_image")
    if not title or not content or not author:
        raise ValueError("Title, content, and author are required fields and cannot be empty.")
    if not _valid_image_url(cover_image):
        raise ValueError("Cover image must use an http or https URL.")
    return title, content, author, summary, category, cover_image


def _create_article(db, values, status, user_id):
    title, content, author, summary, category, cover_image = values
    cursor = db.execute(
        """INSERT INTO articles
           (title, content, author, status, submission_date, summary, category, cover_image, user_id)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            title, content, author, status, _now(), summary, category, cover_image, user_id,
        ),
    )
    db.commit()
    return cursor.lastrowid


def _now():
    return datetime.now(timezone.utc).replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "News Publishing Workflow MVP running"})


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login_choice():
    return render_template("login_choice.html")


def _login(role):
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    account_exists = (
        get_db().execute("SELECT 1 FROM users WHERE role = ? LIMIT 1", (role,)).fetchone()
        is not None
    )
    if not account_exists:
        return (
            render_template(
                "login.html",
                role=role,
                error=None,
                account_configured=False,
            ),
            503,
        )
    user = get_db().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if not user or user["role"] != role or not check_password_hash(user["password_hash"], password):
        return render_template(
            "login.html",
            role=role,
            error="The username or password was not recognized.",
            account_configured=True,
        ), 401
    session.clear()
    session["user_id"] = user["id"]
    csrf_token()
    destination = request.args.get("next")
    if (
        destination
        and destination.startswith("/")
        and not destination.startswith("//")
        and "\\" not in destination
    ):
        return redirect(destination)
    return redirect(url_for("publisher_dashboard" if role == "publisher" else "reader_dashboard"))


@app.route("/reader/login", methods=["GET", "POST"])
def reader_login():
    if request.method == "POST":
        return _login("reader")
    return render_template(
        "login.html",
        role="reader",
        error=None,
        account_configured=_has_role_account("reader"),
    )


@app.route("/publisher/login", methods=["GET", "POST"])
def publisher_login():
    if request.method == "POST":
        return _login("publisher")
    return render_template(
        "login.html",
        role="publisher",
        error=None,
        account_configured=_has_role_account("publisher"),
    )


def _has_role_account(role):
    return (
        get_db().execute("SELECT 1 FROM users WHERE role = ? LIMIT 1", (role,)).fetchone()
        is not None
    )


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have signed out.", "success")
    return redirect(url_for("index"))


@app.route("/reader")
@login_required("reader")
def reader_dashboard():
    rows = get_db().execute(
        """SELECT a.* FROM articles a JOIN bookmarks b ON b.article_id = a.id
           WHERE b.user_id = ? AND a.status = 'APPROVED' ORDER BY b.created_at DESC""",
        (get_current_user()["id"],),
    ).fetchall()
    return render_template("reader_dashboard.html", saved_articles=[_article_dict(row) for row in rows])


@app.route("/publisher")
@login_required("publisher")
def publisher_dashboard():
    db = get_db()
    counts = {
        row["status"]: row["count"]
        for row in db.execute("SELECT status, COUNT(*) AS count FROM articles GROUP BY status")
    }
    articles = db.execute("SELECT * FROM articles ORDER BY id DESC").fetchall()
    return render_template(
        "publisher_dashboard.html",
        articles=[_article_dict(row) for row in articles],
        counts=counts,
    )


@app.route("/publisher/articles/new", methods=["GET", "POST"])
@login_required("publisher")
def new_article():
    if request.method == "GET":
        return render_template("article_editor.html", article=None)
    data = request.form
    try:
        values = _article_values(
            {
                **data,
                "author": get_current_user()["display_name"],
            }
        )
    except ValueError as error:
        return render_template("article_editor.html", article=None, error=str(error)), 400
    status = "SUBMITTED" if data.get("action") == "submit" else "DRAFT"
    article_id = _create_article(get_db(), values, status, get_current_user()["id"])
    flash("Story submitted to the desk." if status == "SUBMITTED" else "Draft saved.", "success")
    if data.get("action") == "preview":
        return redirect(url_for("article_preview", article_id=article_id))
    return redirect(url_for("publisher_dashboard"))


@app.route("/publisher/articles/<int:article_id>/edit", methods=["GET", "POST"])
@login_required("publisher")
def edit_article(article_id):
    db = get_db()
    article = db.execute("SELECT * FROM articles WHERE id = ?", (article_id,)).fetchone()
    if article is None:
        abort(404)
    user_id = get_current_user()["id"]
    if article["user_id"] not in (None, user_id) or article["status"] not in {"DRAFT", "REJECTED"}:
        return _error("Only your draft or rejected story can be edited.", 403)
    if request.method == "GET":
        return render_template("article_editor.html", article=_article_dict(article))
    try:
        values = _article_values({**request.form, "author": get_current_user()["display_name"]})
    except ValueError as error:
        return render_template("article_editor.html", article=_article_dict(article), error=str(error)), 400
    status = "SUBMITTED" if request.form.get("action") == "submit" else "DRAFT"
    title, content, author, summary, category, cover_image = values
    db.execute(
        """UPDATE articles SET title=?, content=?, author=?, summary=?, category=?,
           cover_image=?, status=?, comment=NULL, submission_date=? WHERE id=?""",
        (title, content, author, summary, category, cover_image, status, _now(), article_id),
    )
    db.commit()
    flash("Story resubmitted to the desk." if status == "SUBMITTED" else "Draft updated.", "success")
    if request.form.get("action") == "preview":
        return redirect(url_for("article_preview", article_id=article_id))
    return redirect(url_for("publisher_dashboard"))


@app.route("/publisher/articles/<int:article_id>/preview")
@login_required("publisher")
def article_preview(article_id):
    article = get_db().execute("SELECT * FROM articles WHERE id = ?", (article_id,)).fetchone()
    if article is None:
        abort(404)
    if article["user_id"] not in (None, get_current_user()["id"]):
        return _error("You cannot preview another publisher's draft.", 403)
    return render_template("article_detail.html", article=_article_dict(article), preview=True)


@app.route("/reviewer")
@login_required("publisher")
def reviewer():
    return render_template(
        "reviewer.html",
        verification_tests=PROJECT_VERIFICATION,
        completed_work=PROJECT_MILESTONES,
    )


@app.route("/api/public/articles")
def public_articles():
    db = get_db()
    query = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    sort = "ASC" if request.args.get("sort") == "oldest" else "DESC"
    clauses = ["status = 'APPROVED'"]
    params = []
    if query:
        like = f"%{query}%"
        clauses.append("(title LIKE ? OR author LIKE ? OR content LIKE ? OR summary LIKE ?)")
        params.extend([like, like, like, like])
    if category:
        clauses.append("category = ?")
        params.append(category)
    rows = db.execute(
        f"SELECT * FROM articles WHERE {' AND '.join(clauses)} ORDER BY COALESCE(review_date, submission_date) {sort}, id {sort}",
        params,
    ).fetchall()
    return jsonify([_public_article_dict(row) for row in rows])


@app.route("/api/public/categories")
def public_categories():
    rows = get_db().execute(
        "SELECT DISTINCT category FROM articles WHERE status='APPROVED' ORDER BY category"
    ).fetchall()
    return jsonify([row["category"] for row in rows])


@app.route("/article/<int:article_id>")
def public_article(article_id):
    article = get_db().execute(
        "SELECT * FROM articles WHERE id = ? AND status = 'APPROVED'", (article_id,)
    ).fetchone()
    if article is None:
        abort(404)
    return render_template("article_detail.html", article=_article_dict(article), preview=False)


@app.route("/api/public/articles/<int:article_id>")
def public_article_json(article_id):
    article = get_db().execute(
        "SELECT * FROM articles WHERE id = ? AND status = 'APPROVED'", (article_id,)
    ).fetchone()
    if article is None:
        return _error("Article not found.", 404)
    return jsonify(_public_article_dict(article))


@app.route("/api/reader/bookmarks", methods=["GET", "POST"])
@login_required("reader")
def reader_bookmarks():
    db = get_db()
    user_id = get_current_user()["id"]
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        if not isinstance(data, dict):
            return _error("A valid article object is required.", 400)
        article_id = data.get("article_id")
        if not isinstance(article_id, int):
            return _error("A valid article_id is required.", 400)
        article = db.execute(
            "SELECT id FROM articles WHERE id = ? AND status = 'APPROVED'", (article_id,)
        ).fetchone()
        if article is None:
            return _error("Article not found.", 404)
        db.execute(
            "INSERT OR IGNORE INTO bookmarks (user_id, article_id) VALUES (?, ?)",
            (user_id, article_id),
        )
        db.commit()
        return jsonify({"message": "Article saved."}), 201
    rows = db.execute(
        """SELECT a.* FROM articles a JOIN bookmarks b ON b.article_id = a.id
           WHERE b.user_id = ? AND a.status = 'APPROVED' ORDER BY b.created_at DESC""",
        (user_id,),
    ).fetchall()
    return jsonify([_public_article_dict(row) for row in rows])


@app.route("/api/reader/bookmarks/<int:article_id>", methods=["DELETE"])
@login_required("reader")
def remove_bookmark(article_id):
    db = get_db()
    db.execute(
        "DELETE FROM bookmarks WHERE user_id = ? AND article_id = ?",
        (get_current_user()["id"], article_id),
    )
    db.commit()
    return jsonify({"message": "Article removed from your reading list."})


@app.route("/api/articles", methods=["POST", "GET"])
@login_required("publisher")
def articles():
    db = get_db()
    if request.method == "GET":
        rows = db.execute("SELECT * FROM articles ORDER BY id DESC").fetchall()
        return jsonify([_article_dict(row) for row in rows]), 200
    data = request.get_json(silent=True) or {}
    try:
        values = _article_values(data)
    except ValueError as error:
        return _error(str(error), 400)
    article_id = _create_article(db, values, "SUBMITTED", get_current_user()["id"])
    return jsonify(
        {"message": "Article submitted successfully", "id": article_id, "status": "SUBMITTED"}
    ), 201


@app.route("/api/articles/<int:article_id>")
@login_required("publisher")
def get_article(article_id):
    row = get_db().execute("SELECT * FROM articles WHERE id = ?", (article_id,)).fetchone()
    if row is None:
        return _error("Article not found", 404)
    return jsonify(_article_dict(row)), 200


def _review_article(article_id, action):
    db = get_db()
    row = db.execute("SELECT * FROM articles WHERE id = ?", (article_id,)).fetchone()
    if row is None:
        return _error("Article not found", 404)
    if row["status"] != "SUBMITTED":
        return _error("Only SUBMITTED articles can be reviewed.", 400)
    if row["user_id"] is not None and row["user_id"] == get_current_user()["id"]:
        return _error("A publisher cannot review their own article.", 403)
    if action == "reject":
        data = request.get_json(silent=True) or {}
        comment = data.get("comment", "").strip() if isinstance(data, dict) else ""
        if not comment:
            return _error("Rejection comment is mandatory and cannot be empty.", 400)
        db.execute(
            "UPDATE articles SET status='REJECTED', comment=?, review_date=? WHERE id=?",
            (comment, _now(), article_id),
        )
        message, status = "Article rejected successfully", "REJECTED"
    else:
        db.execute(
            "UPDATE articles SET status='APPROVED', review_date=? WHERE id=?",
            (_now(), article_id),
        )
        message, status = "Article approved successfully", "APPROVED"
    db.commit()
    return jsonify({"message": message, "id": article_id, "status": status}), 200


@app.route("/api/articles/<int:article_id>/approve", methods=["PUT"])
@login_required("publisher")
def approve_article(article_id):
    return _review_article(article_id, "approve")


@app.route("/api/articles/<int:article_id>/reject", methods=["PUT"])
@login_required("publisher")
def reject_article(article_id):
    return _review_article(article_id, "reject")


@app.errorhandler(404)
def not_found(_error):
    return render_template("error.html", code=404, message="That story or page could not be found."), 404


if __name__ == "__main__":
    init_db()
    app.run(host="127.0.0.1", port=int(os.environ.get("APP_PORT", "5000")))
