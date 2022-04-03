CREATE TABLE kayttajat (
    id SERIAL PRIMARY KEY,
    tunnus TEXT,
    etunimi TEXT,
    sukunimi TEXT,
    password TEXT
);

CREATE TABLE vinkit (
    tyyppi TEXT,
    otsikko TEXT,
    tunnus TEXT,
    PRIMARY KEY(tyyppi, otsikko)
);

CREATE TABLE kirjat (
    otsikko TEXT PRIMARY KEY,
    kirjailija TEXT,
    kirjoitusvuosi INTEGER
);