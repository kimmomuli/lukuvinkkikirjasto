from entities.kirjavinkki import Kirjavinkki


# Ei käytetä tyyppivihjeitä vielä tässä vaiheessa
def parse_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi, omistaja):
    try:
        return Kirjavinkki(str(otsikko), str(kirjailija), int(kirjoitusvuosi), str(omistaja))
    except TypeError as error:
        raise TypeError("Väärä syöte") from error
