from werkzeug.security import check_password_hash, generate_password_hash
from database import database


def luo_kayttaja(kayttajatunnus: str, salasana: str) -> str:
    sql = """SELECT tunnus
                FROM kayttajat
                where tunnus = :tunnus"""
    kayttajatietue = database.session.execute(sql, {"tunnus": kayttajatunnus})
    if kayttajatietue.fetchone():
        return "Käyttäjätunnus on jo olemassa"
    if len(salasana) < 6:
        return "Salasanan on oltava vähintään 6 merkkiä pitkä"
    if len(kayttajatunnus) < 4:
        return "Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä"

    salasana_hash = generate_password_hash(salasana)
    sql2 = """INSERT into kayttajat (tunnus, password)
                VALUES (:tunnus, :password)"""
    database.session.execute(
        sql2, {"tunnus": kayttajatunnus, "password": salasana_hash}
    )
    database.session.commit()
    return ""


def login(kayttajatunnus: str, salasana: str) -> bool:
    sql = """SELECT tunnus,password
                FROM kayttajat where tunnus = :tunnus"""
    kayttajatietue = database.session.execute(
        sql, {"tunnus": kayttajatunnus}).fetchone()
    if kayttajatietue:
        return check_password_hash(kayttajatietue[1], salasana)

    return False
