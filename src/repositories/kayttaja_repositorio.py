from werkzeug.security import check_password_hash, generate_password_hash
from database import database


class KayttajaRepository:
    def luo_kayttaja(self, kayttajatunnus: str, salasana: str) -> str:
        sql = """SELECT tunnus
                 FROM kayttajat
                 where tunnus = :tunnus"""
        kayttajatietue = database.session.execute(
            sql, {"tunnus": kayttajatunnus})

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

    def login(self, kayttajatunnus: str, salasana: str) -> bool:
        sql = """SELECT tunnus,password
                 FROM kayttajat where tunnus = :tunnus"""
        kayttajatietue = database.session.execute(
            sql, {"tunnus": kayttajatunnus}).fetchone()
        if kayttajatietue:
            return check_password_hash(kayttajatietue[1], salasana)

        return False

    def poista_kaikki(self) -> None:
        sql = "DELETE FROM kayttajat"
        database.session.execute(sql)
        database.session.commit()


kayttaja_repository = KayttajaRepository()
