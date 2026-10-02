import sqlite3
import os
from flask import Flask, jsonify, request, render_template, g
from datetime import datetime

app = Flask(__name__)
DATABASE = 'app.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
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
        ''')
        db.commit()

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "message": "News Publishing Workflow MVP running"
    })

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/articles', methods=['POST'])
def submit_article():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON payload provided"}), 400

    title = data.get('title', '').strip()
    content = data.get('content', '').strip()
    author = data.get('author', '').strip()

    if not title or not content or not author:
        return jsonify({"error": "Title, content, and author are required fields and cannot be empty."}), 400

    submission_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    status = 'SUBMITTED'

    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        INSERT INTO articles (title, content, author, status, submission_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, author, status, submission_date))
    db.commit()
    article_id = cursor.lastrowid

    return jsonify({
        "message": "Article submitted successfully",
        "id": article_id,
        "status": status
    }), 201

if __name__ == '__main__':
    init_db()
    app.run(host='127.0.0.1', port=5000)
