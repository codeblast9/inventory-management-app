import sqlite3

def validate_user_login(conn, username: str, password: str) -> bool:
    """
    Returns True if the username/password match a user.
    """
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    return cursor.fetchone() is not None

def create_user(conn, username: str, password: str):
    """
    Creates a new user (operator).
    """
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )
    conn.commit()

def get_all_users(conn):
    """
    Returns all usernames.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users")
    return cursor.fetchall()
