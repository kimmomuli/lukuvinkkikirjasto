import unittest
from repositories.kayttaja_repositorio import kayttaja_repository


class TestKayttajaRepository(unittest.TestCase):
    def setUp(self):
        kayttaja_repository.poista_kaikki()
        kayttaja_repository.luo_kayttaja("kayttajanimi", "salasana")

    def test_sisaankirjautuminen_oikealla_kayttajanimella_ja_salasanalla(self):
        tulos = kayttaja_repository.kirjaudu_sisaan("kayttajanimi", "salasana")
        self.assertTrue(tulos)

    def test_sisaankirjautuminen_vaaralla_kayttajanimella(self):
        tulos = kayttaja_repository.kirjaudu_sisaan("väärä", "salasana")
        self.assertFalse(tulos)

    def test_sisaankirjautuminen_vaaralla_salasanalla(self):
        tulos = kayttaja_repository.kirjaudu_sisaan("kayttajanimi", "väärä")
        self.assertFalse(tulos)

    def test_kayttaja_on_olemassa_kun_kayttaja_on_olemassa(self):
        tulos = kayttaja_repository.kayttaja_on_olemassa("kayttajanimi")
        self.assertTrue(tulos)

    def test_kayttaja_on_olemassa_kun_kayttaja_ei_ole_olemassa(self):
        tulos = kayttaja_repository.kayttaja_on_olemassa("väärä")
        self.assertFalse(tulos)
