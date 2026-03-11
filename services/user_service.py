from flask_bcrypt import generate_password_hash, check_password_hash
import MySQLdb.cursors
from flask import current_app as app

def register_user(db, username, email, password):
    cursor = db.cursor()
    pw_hash = generate_password_hash(password).decode('utf-8')
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)",
            (username, email, pw_hash)
        )
        db.commit()
        return {"message": "User created"}
    except MySQLdb.IntegrityError:
        return {"error": "Username or email already exists"}

def login_user(db, email, password):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user and check_password_hash(user['password_hash'], password):
        return {"id": user['id'], "username": user['username'], "email": user['email']}
    return None

def add_user_match(db, user_id, sport, opponent, score, result, match_date):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO user_matches (user_id, sport, opponent, score, result, match_date) VALUES (%s, %s, %s, %s, %s, %s)",
        (user_id, sport, opponent, score, result, match_date)
    )
    db.commit()
    return {"message": "Match added"}

def get_user_matches(db, user_id):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM user_matches WHERE user_id=%s ORDER BY match_date DESC", (user_id,))
    return cursor.fetchall()