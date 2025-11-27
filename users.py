from werkzeug.security import check_password_hash, generate_password_hash
import db

def create_user(username, password):
    password_hash = generate_password_hash(password)
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    db.execute(sql, [username, password_hash])

def check_login(username, password):
    sql = "SELECT id, password_hash FROM users WHERE username = ?"
    result = db.query(sql, [username])

    if len(result) == 1:
        user_id, password_hash = result[0]
        if check_password_hash(password_hash, password):
            return user_id

    return None

def get_user(user_id):
    sql = "SELECT username, id AS user_id FROM users WHERE id = ?"
    result = db.query(sql, [user_id])
    return result[0] if result else None

def get_threads(user_id):
    sql = """SELECT t.id AS thread_id,
                    t.title,
                    t.comment,
                    t.user_id AS user_id,
                    IFNULL(COUNT(m.id), 0) total
             FROM threads t LEFT JOIN messages m
             ON t.id = m.thread_id
             WHERE t.user_id = ?
             GROUP BY t.id;"""
    
    result = db.query(sql, [user_id])
    return result if result else None
