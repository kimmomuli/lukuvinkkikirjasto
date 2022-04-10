from typing import List
from database import database
from entities.kirjavinkki import Kirjavinkki
from datetime import datetime as dt


def lataa_kirjat() -> List[Kirjavinkki]:
    sql = "SELECT a.otsikko, a.kirjailija, a.kirjoitusvuosi, b.tunnus FROM kirjat as a INNER JOIN vinkit as b ON a.otsikko = b.otsikko ORDER BY luontiaika"
    tulos = database.session.execute(sql)
    vinkit = tulos.fetchall()
    kirjavinkit = []
    for vinkki in vinkit:
        kirjavinkit.append(Kirjavinkki(
            vinkki["otsikko"], vinkki["kirjailija"], vinkki["kirjoitusvuosi"], vinkki["tunnus"]))
    return kirjavinkit


def tallenna_kirjavinkki(kirjavinkki: Kirjavinkki):
    sql = "INSERT INTO vinkit (tyyppi, otsikko, tunnus, luontiaika) VALUES (:tyyppi, :otsikko, :tunnus, :luontiaika) "
    database.session.execute(
        sql, {"tyyppi": "kirja", "otsikko": kirjavinkki.otsikko, "tunnus": kirjavinkki.omistaja, "luontiaika": dt.now()})
    sql2 = "INSERT INTO kirjat (otsikko,kirjailija,kirjoitusvuosi) VALUES (:otsikko, :kirjailija, :kirjoitusvuosi)"
    database.session.execute(sql2, {"otsikko": kirjavinkki.otsikko,
                             "kirjailija": kirjavinkki.kirjailija, "kirjoitusvuosi": kirjavinkki.kirjoitusvuosi})
    database.session.commit()
