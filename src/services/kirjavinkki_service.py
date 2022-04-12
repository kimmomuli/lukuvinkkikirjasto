
def tarkista_numeromuoto(numero) -> bool:
    try:
        numero = int(numero)
        return True
    except:  # pylint: disable=bare-except
        return False


def tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi) -> str:
    if len(str(otsikko)) < 2:
        return "Otsikon tulee sisältää ainakin kaksi merkkiä"

    if len(str(kirjailija)) < 2:
        return "Kirjailijan tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_numeromuoto(kirjoitusvuosi):
        return "Kirjoitusvuosi pitää olla numero"
    if not 1 < int(kirjoitusvuosi) < 2025:
        return "Kirjoitusvuosi pitää olla numero väliltä 1-2025"

    return ""
