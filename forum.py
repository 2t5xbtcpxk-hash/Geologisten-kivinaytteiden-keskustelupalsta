import db


def get_threads(page, page_size):
    sql = """SELECT t.id id, t.user_id user_id, t.title, c.rocktype rocktype, t.rock rock, 
             IFNULL(COUNT(m.id), 0) total, IFNULL(MAX(m.sent_at), "-") last
             FROM threads t LEFT JOIN messages m
                            ON t.id = m.thread_id
                            LEFT JOIN classes as c 
                            ON t.classes_id = c.id
             GROUP BY t.id
             ORDER BY t.id DESC
             LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

def add_thread(title, comment, user_id, rock_type, rock,
               latitude, longitude, collection_date):
    sql = """INSERT INTO threads (title, comment, user_id, classes_id, rock, latitude, longitude, collection_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    db.execute(sql, [title, comment, user_id, rock_type, rock, latitude, longitude, collection_date])
    thread_id = db.last_insert_id()
    return thread_id
    
def add_message(content, user_id, thread_id):
    sql = """INSERT INTO messages (content, sent_at, user_id, thread_id)
             VALUES (?, datetime('now'), ?, ?)"""
    db.execute(sql, [content, user_id, thread_id])

def add_image(thread_id, sample_image, user_id):
    sql = """INSERT INTO images (thread_id, sample_image, user_id) 
              VALUES (?, ?, ?)"""
    db.execute(sql, [thread_id, sample_image, user_id])

def get_thread(thread_id):
    sql = """SELECT t.id, t.title, t.comment, t.user_id user_id, t.rock, c.rocktype rocktype,
             t.latitude, t.longitude, t.collection_date 
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

def get_images(thread_id):
    sql = """SELECT id
             FROM images
             WHERE thread_id = ?"""
    result = db.query(sql, [thread_id])
    return result

def get_image(image_id):
    sql = """SELECT id, sample_image, thread_id
             FROM images
             WHERE id = ?"""
    result = db.query(sql, [image_id])
    return result[0][1] if result else None

def get_image2(image_id):
    sql = """SELECT id, user_id, thread_id
             FROM images
             WHERE id = ?"""
    result = db.query(sql, [image_id])
    return result[0]

def remove_image(image_id):
    sql = "DELETE FROM images WHERE id = ?"
    db.execute(sql, [image_id])

def thread_count():
    sql = "SELECT COUNT(*) FROM threads"
    return db.query(sql)[0][0]

def thread_image_count(thread_id):
    sql = "SELECT IFNULL(COUNT(*), 0) FROM images WHERE thread_id = ?"
    return db.query(sql, [thread_id])[0][0]