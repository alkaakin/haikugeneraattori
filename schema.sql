CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE haikut (
    id INTEGER,
    nimi TEXT,
    arvosana INTEGER,
    genre TEXT,
    visible INTEGER,
    content TEXT
);