CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);
CREATE TABLE tips (
    type TEXT,
    title TEXT,
    author TEXT,
    adder_username TEXT,
    timestamp TIMESTAMP,
    PRIMARY KEY (type, title, adder_username)
);
CREATE TABLE book_tips (
    title TEXT,
    author TEXT,
    year INTEGER,
    PRIMARY KEY (title, author)
);