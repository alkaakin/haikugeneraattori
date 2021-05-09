CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE haikut (
    id SERIAL PRIMARY KEY,
    nimi TEXT,
    genre TEXT,
    content TEXT,
    ratings INTEGER,
    active BOOLEAN,
    sum INTEGER,
    arvosana NUMERIC
);