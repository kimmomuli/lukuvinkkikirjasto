from sqlalchemy import false, true
from entities.kirjavinkki import Kirjavinkki
import string


# Ei käytetä tyyppivihjeitä vielä tässä vaiheessa
def parse_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi, omistaja):
    try:
        return Kirjavinkki(str(otsikko), str(kirjailija), int(kirjoitusvuosi), str(omistaja))
    except TypeError as error:
        raise TypeError("Väärä syöte") from error

def tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi):
    virheet = []
    sallitut_merkit = string.ascii_letters+string.whitespace
    sisaltaako_vuosi_numeroita = true
    if len(otsikko) < 2:
        virheet.append("Otsikon tulee sisältää ainakin kaksi merkkiä")
    if len(kirjailija) < 2:
        virheet.append("Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä")
    if not all (merkki in sallitut_merkit for merkki in kirjailija):
        virheet.append("Kirjailijan nimi voi sisältää vain kirjaimia tai välilyöntejä")
    if not all (merkki in string.digits for merkki in kirjoitusvuosi):
        sisaltaako_vuosi_numeroita = false
        virheet.append("Kirjoitusvuosi ei voi sisältää muita merkkejä kuin numeroita")
    if len(kirjoitusvuosi) == 0:
        sisaltaako_vuosi_numeroita = false
        virheet.append("Vuosi ei voi olla 0")
    if sisaltaako_vuosi_numeroita == true:
        if int(kirjoitusvuosi)<0 or int(kirjoitusvuosi)>2025:
            virheet.append("Kirjan tulee olla kirjoitettu 1-2025 välisinä vuosina")
    if not virheet:
        return []
    return virheet


