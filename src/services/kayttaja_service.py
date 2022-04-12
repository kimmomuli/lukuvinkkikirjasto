from repositories.kayttaja_repositorio import KayttajaRepository
from repositories.kayttaja_repositorio import kayttaja_repository as default_kayttaja_repository


class KayttajaService:
    def __init__(self,
                 kayttaja_repository: KayttajaRepository = default_kayttaja_repository) -> None:
        self.kayttaja_repository = kayttaja_repository

    def luo_kayttaja(self, kayttajatunnus: str, salasana: str) -> str:
        if self.kayttaja_repository.kayttaja_on_olemassa(kayttajatunnus):
            return "Käyttäjätunnus on jo olemassa"
        if len(salasana) < 6:
            return "Salasanan on oltava vähintään 6 merkkiä pitkä"
        if len(kayttajatunnus) < 4:
            return "Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä"

        self.kayttaja_repository.luo_kayttaja(kayttajatunnus, salasana)
        return ""

    def kirjaudu_sisaan(self, kayttajatunnus: str, salasana: str) -> str:
        tulos = self.kayttaja_repository.kirjaudu_sisaan(
            kayttajatunnus, salasana)
        if not tulos:
            return "Väärä käyttäjätunnus tai salasana"
        return ""


kayttaja_service = KayttajaService()
