#
class Kirjavinkki:
    def __init__(self, otsikko: str, kirjailija: str = "tuntematon", kirjoitusvuosi: int = 1981, omistaja: str = ""):
        self.otsikko: str = otsikko
        self.kirjailija: str = kirjailija
        self.kirjoitusvuosi: int = kirjoitusvuosi
        self.omistaja: str = omistaja
        self.tyyppi: str = "kirja"
