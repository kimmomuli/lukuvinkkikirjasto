from werkzeug.security import check_password_hash, generate_password_hash
from database import database


class KayttajaRepository:
    def kayttaja_on_olemassa(self, kayttajatunnus: str) -> bool:
        sql = """SELECT tunnus
                 FROM kayttajat
                 where tunnus = :tunnus"""
        kayttajatietue = database.session.execute(
            sql, {"tunnus": kayttajatunnus})

        return bool(kayttajatietue.fetchone())

    def luo_kayttaja(self, kayttajatunnus: str, salasana: str) -> None:
        salasana_hash = generate_password_hash(salasana)
        sql2 = """INSERT into kayttajat (tunnus, password)
                  VALUES (:tunnus, :password)"""
        database.session.execute(
            sql2, {"tunnus": kayttajatunnus, "password": salasana_hash}
        )
        database.session.commit()

    def kirjaudu_sisaan(self, kayttajatunnus: str, salasana: str) -> bool:
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
