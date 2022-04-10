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
    tekija TEXT,
    tunnus TEXT,
    luontiaika TIMESTAMP,
    PRIMARY KEY(tyyppi, otsikko,tunnus)
);

CREATE TABLE kirjat (
    otsikko TEXT,
    kirjailija TEXT,
    kirjoitusvuosi INTEGER,
    PRIMARY KEY(otsikko,kirjailija)
);