from database import database


def drop_tables():
    sql = "DROP TABLE IF EXISTS kayttajat, vinkit, kirjat"
    database.session.execute(sql)
    database.session.commit()


def create_tables():
    with open("schema.sql", "r", encoding="utf8") as schema_file:
        schema = schema_file.readlines()

    database.session.execute(''.join(schema))
    database.session.commit()


def initialize_database():
    drop_tables()
    create_tables()
