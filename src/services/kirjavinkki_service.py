from entities.kirjavinkki import Kirjavinkki
from repositories.vinkki_repositorio import VinkkiRepositorio
from repositories.vinkki_repositorio import vinkki_repositorio as default_vinkki_repositorio


class KirjavinkkiService:
    def __init__(self, vinkki_repositorio: VinkkiRepositorio = default_vinkki_repositorio) -> None:
        self.vinkki_repositorio = vinkki_repositorio

    def lisaa_kirjavinkki(self, otsikko: str, kirjailija: str, kirjoitusvuosi: str, omistaja: str) -> str:
        if len(otsikko) < 2:
            return "Otsikon tulee sisältää ainakin kaksi merkkiä"
        if len(kirjailija) < 2:
            return "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä"

        if not str.isdigit(kirjoitusvuosi):
            return "Kirjoitusvuoden pitää olla numero"
        if not 1 <= int(kirjoitusvuosi) <= 2025:
            return "Kirjoitusvuoden pitää olla numero väliltä 1-2025"

        kirjavinkki = Kirjavinkki(
            otsikko, kirjailija, kirjoitusvuosi, omistaja
        )
        tulos = self.vinkki_repositorio.tallenna_kirjavinkki(kirjavinkki)
        if not tulos:
            return "Olet jo lisännyt kirjavinkin samalla otsikolla"
        return ""


kirjavinkki_service = KirjavinkkiService()
