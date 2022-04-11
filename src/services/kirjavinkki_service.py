def tarkista_merkkijonomuoto(sana) -> bool:
    try:
        sana = str(sana)
        return True
    except:
        return False


def tarkista_numeromuoto(numero) -> bool:
    try:
        numero = int(numero)
        return True
    except:
        return False


def tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi):
    # Otsikko ja kirjailija voivat sisältää numeroita, kun ne vain ovat merkkijonomuodossa!

    if not tarkista_merkkijonomuoto(otsikko) and len(otsikko) < 2:
        return "Otsikon pitää olla merkkijono ja sen tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_merkkijonomuoto(kirjailija) and len(kirjailija) < 2:
        return "Kirjailijan pitää olla merkkijono ja sen tulee sisältää ainakin kaksi merkkiä"

    if not tarkista_numeromuoto(kirjoitusvuosi):
        return "Kirjoitusvuosi pitää olla numero"
    elif not (1 < int(kirjoitusvuosi) < 2025):
        return "Kirjoitusvuosi pitää olla numero väliltä 1-2025"

    return ""
