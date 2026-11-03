"""Create a local NewsFlow reader or publisher account without storing passwords."""

import argparse
import getpass

from werkzeug.security import generate_password_hash

from src.app import app, get_db, init_db


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=("reader", "publisher"), required=True)
    parser.add_argument("--username", required=True)
    parser.add_argument("--name", required=True, dest="display_name")
    args = parser.parse_args()
    username = args.username.strip()
    display_name = args.display_name.strip()
    if not username or not display_name:
        parser.error("Username and display name cannot contain only whitespace.")
    password = getpass.getpass("Password: ")
    confirmation = getpass.getpass("Confirm password: ")
    if len(password) < 12:
        parser.error("Choose a password with at least 12 characters.")
    if password != confirmation:
        parser.error("Passwords do not match.")

    with app.app_context():
        init_db()
        db = get_db()
        try:
            db.execute(
                "INSERT INTO users (username, password_hash, role, display_name) VALUES (?, ?, ?, ?)",
                (username, generate_password_hash(password), args.role, display_name),
            )
            db.commit()
        except Exception:
            db.rollback()
            raise
    print(f"Created {args.role} account '{username}'.")


if __name__ == "__main__":
    main()
