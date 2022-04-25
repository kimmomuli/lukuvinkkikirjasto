CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);
CREATE TABLE tips (
    id SERIAL PRIMARY KEY,
    type TEXT,
    title TEXT,
    author TEXT,
    adder_username TEXT,
    timestamp TIMESTAMP,
    UNIQUE (type, title, author, adder_username)
);
CREATE TABLE book_tips (
    title TEXT,
    author TEXT,
    year INTEGER,
    PRIMARY KEY (title, author)
);
CREATE TABLE likes (
    tip_id INT REFERENCES tips,
    username TEXT,
    PRIMARY KEY(tip_id, username)
);