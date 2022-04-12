import unittest
from repositories.kayttaja_repositorio import kayttaja_repository


class TestKayttajaRepo(unittest.TestCase):
    def setUp(self):
        kayttaja_repository.poista_kaikki()

    def test_liian_lyhyt_kayttajatunnus_ei_kelpaa(self):
        virheviesti = kayttaja_repository.luo_kayttaja("ea", "PutinOnNilkki")
        self.assertEqual(
            virheviesti, "Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä"
        )

    def test_liian_lyhyt_salasana_ei_kelpaa(self):
        virheviesti = kayttaja_repository.luo_kayttaja("Zelenskyi", "Putin")
        self.assertEqual(
            virheviesti, "Salasanan on oltava vähintään 6 merkkiä pitkä"
        )

    def test_uuden_kayttajan_luonti_onnistuu(self):
        virheviesti = kayttaja_repository.luo_kayttaja(
            "Zelenskyi", "PutinOnNilkki"
        )
        self.assertEqual(virheviesti, "")

    def test_voi_luoda_kayttajan_ja_logata_sisaan(self):
        kayttaja_repository.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        tulos = kayttaja_repository.login("Zelenskyi", "PutinOnNilkki")
        self.assertTrue(tulos)

    def test_vaaralla_salasanalla_ei_paase(self):
        kayttaja_repository.luo_kayttaja("Zelenskyi", "PutinOnNilkki")

        tulos = kayttaja_repository.login("Zelenskyi", "PutinOnKiva")
        self.assertFalse(tulos)

    def test_ei_voi_luoda_samaa_kayttajaa_kahdesti(self):
        kayttaja_repository.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        virheviesti = kayttaja_repository.luo_kayttaja(
            "Zelenskyi", "PutinOnKakka"
        )
        self.assertEqual(virheviesti, "Käyttäjätunnus on jo olemassa")

    def test_kirjautuminen_vaaralla_tunnuksella(self):
        tulos = kayttaja_repository.login("Putin", "PutininSalasana")
        self.assertFalse(tulos)
