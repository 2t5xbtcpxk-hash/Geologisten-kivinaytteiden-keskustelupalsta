CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE IF NOT EXISTS threads (
    id INTEGER PRIMARY KEY,
    title TEXT,
    rock TEXT,
    comment TEXT,
    classes_id TEXT REFERENCES classes,
    latitude TEXT,
    longitude TEXT,
    collection_date TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY,
    sample_image BLOB,
    thread_id INTEGER REFERENCES threads ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY,
    content TEXT,
    sent_at TEXT,
    user_id INTEGER REFERENCES users,
    thread_id INTEGER REFERENCES threads ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS classes (
    id INTEGER PRIMARY KEY,
    title TEXT,
    rocktype TEXT
);