import unittest
from services.kayttaja_service import KayttajaService


class StubKayttajaRepository:
    def __init__(self) -> None:
        self.kayttajat = []

    def kayttaja_on_olemassa(self, kayttajatunnus: str) -> bool:
        for kayttaja in self.kayttajat:
            if kayttaja[0] == kayttajatunnus:
                return True
        return False

    def luo_kayttaja(self, kayttajatunnus: str, salasana: str) -> None:
        self.kayttajat.append((kayttajatunnus, salasana))

    def kirjaudu_sisaan(self, kayttajatunnus: str, salasana: str) -> bool:
        for kayttaja in self.kayttajat:
            if kayttaja[0] == kayttajatunnus and kayttaja[1] == salasana:
                return True
        return False


class TestKayttajaService(unittest.TestCase):
    def setUp(self):
        self.kayttaja_service = KayttajaService(StubKayttajaRepository())

    def test_liian_lyhyt_kayttajatunnus_ei_kelpaa(self):
        virheviesti = self.kayttaja_service.luo_kayttaja("ea", "PutinOnNilkki")
        self.assertEqual(
            virheviesti, "Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä"
        )

    def test_liian_lyhyt_salasana_ei_kelpaa(self):
        virheviesti = self.kayttaja_service.luo_kayttaja("Zelenskyi", "Putin")
        self.assertEqual(
            virheviesti, "Salasanan on oltava vähintään 6 merkkiä pitkä"
        )

    def test_uuden_kayttajan_luonti_onnistuu(self):
        virheviesti = self.kayttaja_service.luo_kayttaja(
            "Zelenskyi", "PutinOnNilkki"
        )
        self.assertEqual(virheviesti, "")

    def test_voi_luoda_kayttajan_ja_logata_sisaan(self):
        self.kayttaja_service.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        virheviesti = self.kayttaja_service.kirjaudu_sisaan(
            "Zelenskyi", "PutinOnNilkki")
        self.assertEqual(virheviesti, "")

    def test_vaaralla_salasanalla_ei_paase(self):
        self.kayttaja_service.luo_kayttaja("Zelenskyi", "PutinOnNilkki")

        virheviesti = self.kayttaja_service.kirjaudu_sisaan(
            "Zelenskyi", "PutinOnKiva")
        self.assertEqual(virheviesti, "Väärä käyttäjätunnus tai salasana")

    def test_ei_voi_luoda_samaa_kayttajaa_kahdesti(self):
        self.kayttaja_service.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        virheviesti = self.kayttaja_service.luo_kayttaja(
            "Zelenskyi", "PutinOnKakka"
        )
        self.assertEqual(virheviesti, "Käyttäjätunnus on jo olemassa")

    def test_kirjautuminen_vaaralla_tunnuksella(self):
        virheviesti = self.kayttaja_service.kirjaudu_sisaan(
            "Putin", "PutininSalasana")
        self.assertEqual(virheviesti, "Väärä käyttäjätunnus tai salasana")
