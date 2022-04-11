def tarkista_merkkijonomuoto(sana) -> bool:
    if type(sana) == str:
        return True
    return False


def tarkista_numeromuoto(numero) -> bool:
    if type(numero) == int:
        return True
    return False


def tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi) -> str:

    if not tarkista_merkkijonomuoto(otsikko):
        return "Otsikon pitää olla merkkijono"
    elif len(otsikko) < 2:
        return "Otsikon tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_merkkijonomuoto(kirjailija):
        return "Kirjailijan pitää olla merkkijono"
    elif len(kirjailija) < 2:
        return "Kirjailijan tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_numeromuoto(kirjoitusvuosi):
        return "Kirjoitusvuosi pitää olla numero"
    elif not (1 < int(kirjoitusvuosi) < 2025):
        return "Kirjoitusvuosi pitää olla numero väliltä 1-2025"

    return ""
