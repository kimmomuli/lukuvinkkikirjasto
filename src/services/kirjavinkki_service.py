class KirjavinkkiService:
    def tarkista_numeromuoto(self, numero: int) -> bool:
        try:
            numero = int(numero)
            return True
        except ValueError:
            return False

    def tarkista_kirjavinkki(self, otsikko: str, kirjailija: str, kirjoitusvuosi: str) -> str:
        if len(str(otsikko)) < 2:
            return "Otsikon tulee sisältää ainakin kaksi merkkiä"

        if len(str(kirjailija)) < 2:
            return "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä"

        if not self.tarkista_numeromuoto(kirjoitusvuosi):
            return "Kirjoitusvuoden pitää olla numero"
        if not 1 < int(kirjoitusvuosi) < 2025:
            return "Kirjoitusvuoden pitää olla numero väliltä 1-2025"

        return ""


kirjavinkki_service = KirjavinkkiService()
