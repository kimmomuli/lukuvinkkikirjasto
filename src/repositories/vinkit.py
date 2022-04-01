from database import database
from entities.kirjavinkki import Kirjavinkki


def lataa_kirjat() -> list[Kirjavinkki]:
    sql = "SELECT a.otsikko, a.kirjailija, a.kirjoitusvuosi, b.tunnus FROM kirjat as a INNER JOIN vinkit as b ON a.otsikko = b.otsikko "
    tulos = database.session.execute(sql)
    vinkit = tulos.fetchall()
    kirjavinkit = []
    for vinkki in vinkit:
        kirjavinkit.append(Kirjavinkki(
            vinkki["otsikko"], vinkki["kirjailija"], vinkki["kirjoitusvuosi"], vinkki["tunnus"]))
    return kirjavinkit


def tallenna_kirjavinkki(kirjavinkki: Kirjavinkki):
    sql = "INSERT INTO vinkit (tyyppi, otsikko, tunnus) VALUES (:tyyppi, :otsikko, :tunnus) "
    database.session.execute(
        sql, {"tyyppi": "kirja", "otsikko": kirjavinkki.otsikko, "tunnus": kirjavinkki.omistaja})
    sql2 = "INSERT INTO kirjat (otsikko,kirjailija,kirjoitusvuosi) VALUES (:otsikko, :kirjailija, :kirjoitusvuosi)"
    database.session.execute(sql2, {"otsikko": kirjavinkki.otsikko,
                             "kirjailija": kirjavinkki.kirjailija, "kirjoitusvuosi": kirjavinkki.kirjoitusvuosi})
    database.commit()
