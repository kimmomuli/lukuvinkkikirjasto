from typing import List
from datetime import datetime as dt
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation  # pylint: disable=no-name-in-module
from database import database
from entities.kirjavinkki import Kirjavinkki


class VinkkiRepositorio:
    def lataa_kirjat(self) -> List[Kirjavinkki]:
        sql = """SELECT a.otsikko, a.kirjailija, a.kirjoitusvuosi, b.luontiaika, b.tunnus
                 FROM kirjat as a INNER JOIN vinkit as b ON a.otsikko = b.otsikko AND a.kirjailija = b.tekija
                 ORDER BY luontiaika DESC"""
        tulos = database.session.execute(sql)
        vinkit = tulos.fetchall()
        kirjavinkit = []
        for vinkki in vinkit:
            kirjavinkit.append(Kirjavinkki(
                vinkki["otsikko"], vinkki["kirjailija"], vinkki["kirjoitusvuosi"], vinkki["tunnus"], vinkki["luontiaika"]))
        return kirjavinkit

    def tallenna_kirjavinkki(self, kirjavinkki: Kirjavinkki) -> bool:
        try:
            sql = """INSERT INTO vinkit (tyyppi, otsikko, tekija, tunnus, luontiaika)
                     VALUES (:tyyppi, :otsikko, :tekija, :tunnus, :luontiaika)"""
            database.session.execute(
                sql,
                {
                    "tyyppi": "kirja",
                    "otsikko": kirjavinkki.otsikko,
                    "tekija": kirjavinkki.kirjailija,
                    "tunnus": kirjavinkki.omistaja,
                    "luontiaika": dt.now()
                }
            )

            sql2 = """INSERT INTO kirjat (otsikko, kirjailija, kirjoitusvuosi)
                      VALUES (:otsikko, :kirjailija, :kirjoitusvuosi) ON CONFLICT DO NOTHING"""
            database.session.execute(
                sql2,
                {
                    "otsikko": kirjavinkki.otsikko,
                    "kirjailija": kirjavinkki.kirjailija,
                    "kirjoitusvuosi": kirjavinkki.kirjoitusvuosi
                }
            )
            database.session.commit()
            return True
        except IntegrityError as error:
            # UNIQUE constraint fail
            assert isinstance(error.orig, UniqueViolation)
            database.session.rollback()
            return False

    def poista_kaikki(self) -> None:
        sql = "DELETE FROM kirjat;DELETE FROM vinkit"
        database.session.execute(sql)
        database.session.commit()

    # def poista_vinkki(self, vinkki):
    #    pass


vinkki_repositorio = VinkkiRepositorio()
