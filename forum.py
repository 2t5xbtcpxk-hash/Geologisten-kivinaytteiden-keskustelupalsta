import db


def get_threads():
    sql = """SELECT t.id id, t.user_id user_id, t.title, c.rocktype rocktype, t.rock rock, IFNULL(COUNT(m.id), 0) total, IFNULL(MAX(m.sent_at), "-") last
             FROM threads t LEFT JOIN messages m
                            ON t.id = m.thread_id
                            LEFT JOIN classes as c 
                            ON t.classes_id = c.id
             GROUP BY t.id
             ORDER BY t.id DESC"""
    return db.query(sql)

def add_thread(title, comment, user_id, rock_type, rock, latitude, longitude, collection_date, sample_image):
    sql = "INSERT INTO threads (title, comment, user_id, classes_id, rock, latitude, longitude, collection_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    db.execute(sql, [title, comment, user_id, rock_type, rock, latitude, longitude, collection_date])
    thread_id = db.last_insert_id()
    sql2 = "INSERT INTO images (thread_id, sample_image) VALUES (?, ?)"
    db.execute(sql2, [thread_id, sample_image])
    return thread_id
    
def add_message(content, user_id, thread_id):
    sql = """INSERT INTO messages (content, sent_at, user_id, thread_id)
             VALUES (?, datetime('now'), ?, ?)"""
    db.execute(sql, [content, user_id, thread_id])

def get_thread(thread_id):
    sql = """SELECT t.id, t.title, t.comment, t.user_id, t.rock, c.rocktype rocktype, t.latitude, t.longitude, t.collection_date 
             FROM threads t LEFT JOIN classes c
                            ON t.classes_id = c.id
             WHERE t.id = ?"""
    result = db.query(sql, [thread_id])
    return result[0] if result else None

def get_messages(thread_id):
    sql = """SELECT m.id, m.content, m.sent_at, m.user_id, u.username
             FROM messages m, users u
             WHERE m.user_id = u.id AND m.thread_id = ?
             ORDER BY m.id"""
    return db.query(sql, [thread_id])

def get_message(message_id):
    sql = """SELECT id, content, thread_id, user_id
             FROM messages
             WHERE id = ?"""
    result = db.query(sql, [message_id])
    return result[0] if result else None

def update_message(message_id, content):
    sql = "UPDATE messages SET content = ? WHERE id = ?"
    db.execute(sql, [content, message_id])

def remove_message(message_id):
    sql = "DELETE FROM messages WHERE id = ?"
    db.execute(sql, [message_id])

def remove_thread(thread_id):
    sql = "DELETE FROM threads WHERE id = ?"
    db.execute(sql, [thread_id])

def update_thread(thread_id, title, comment, rock, rock_type, latitude, longitude, collection_date, image_file):
    sql = "UPDATE threads SET title = ? WHERE id = ?"
    db.execute(sql, [title, thread_id])
    sql = "UPDATE threads SET comment = ? WHERE id = ?"
    db.execute(sql, [comment, thread_id])
    sql = "UPDATE threads SET rock = ? WHERE id = ?"
    db.execute(sql, [rock, thread_id])
    sql = "UPDATE threads SET classes_id = ? WHERE id = ?"
    db.execute(sql, [rock_type, thread_id])
    sql = "UPDATE threads SET rock = ? WHERE id = ?"
    db.execute(sql, [rock, thread_id])
    sql = "UPDATE threads SET latitude = ? WHERE id = ?"
    db.execute(sql, [latitude, thread_id])
    sql = "UPDATE threads SET longitude = ? WHERE id = ?"
    db.execute(sql, [longitude, thread_id])
    sql = "UPDATE threads SET collection_date = ? WHERE id = ?"
    db.execute(sql, [collection_date, thread_id])
    sql = "UPDATE images SET sample_image = ? WHERE thread_id = ?"
    db.execute(sql, [image_file, thread_id])

def update_thread_no_image(thread_id, title, comment, rock, rock_type, latitude, longitude, collection_date):
    sql = "UPDATE threads SET title = ? WHERE id = ?"
    db.execute(sql, [title, thread_id])
    sql = "UPDATE threads SET comment = ? WHERE id = ?"
    db.execute(sql, [comment, thread_id])
    sql = "UPDATE threads SET rock = ? WHERE id = ?"
    db.execute(sql, [rock, thread_id])
    sql = "UPDATE threads SET classes_id = ? WHERE id = ?"
    db.execute(sql, [rock_type, thread_id])
    sql = "UPDATE threads SET rock = ? WHERE id = ?"
    db.execute(sql, [rock, thread_id])
    sql = "UPDATE threads SET latitude = ? WHERE id = ?"
    db.execute(sql, [latitude, thread_id])
    sql = "UPDATE threads SET longitude = ? WHERE id = ?"
    db.execute(sql, [longitude, thread_id])
    sql = "UPDATE threads SET collection_date = ? WHERE id = ?"
    db.execute(sql, [collection_date, thread_id])

def search(query):
    sql = """SELECT t.title,
                    t.id thread_id,
                    c.rocktype
             FROM threads t LEFT JOIN classes c
                            ON t.classes_id = c.id
             WHERE t.title LIKE ? OR
                   t.rock LIKE ? OR
                   c.rocktype LIKE ?
             ORDER BY t.title DESC"""
    like = "%" + query + "%"
    return db.query(sql, [like, like, like])

def get_user(user_id):
    sql = """SELECT username
             FROM users
             WHERE id = ?"""
    result = db.query(sql, [user_id])
    return result[0]

def get_image(thread_id):
    sql = """SELECT id, sample_image, thread_id
             FROM images
             WHERE thread_id = ?"""
    result = db.query(sql, [thread_id])
    return result[0][0]