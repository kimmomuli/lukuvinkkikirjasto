from datetime import date

def tarkista_merkkijonomuoto(sana) -> bool:
    if isinstance(sana, str):
        return True
    return False


def tarkista_numeromuoto(numero) -> bool:
    if isinstance(numero, int):
        return True
    return False


def tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi) -> str:
    three_years_from_this_year = int(date.today().year) + 3

    if not tarkista_merkkijonomuoto(otsikko):
        return "Otsikon pitää olla merkkijono"
    if len(otsikko) < 2:
        return "Otsikon tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_merkkijonomuoto(kirjailija):
        return "Kirjailijan pitää olla merkkijono"
    if len(kirjailija) < 2:
        return "Kirjailijan tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_numeromuoto(kirjoitusvuosi):
        return "Kirjoitusvuosi pitää olla numero"
    if not 1 < int(kirjoitusvuosi) < three_years_from_this_year:
        return "Kirjoitusvuosi pitää olla numero väliltä 1-2025"

    return ""
