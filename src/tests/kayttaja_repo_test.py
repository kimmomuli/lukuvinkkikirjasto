import flask_testing
from flask import Flask
import repositories.kayttajat
from initialize_database import initialize_database
from app import create_app


class TestKayttajaRepo(flask_testing.TestCase):
    def create_app(self):
        return create_app(testing=True)

    def setUp(self):
        initialize_database()

    def test_liian_lyhyt_kayttajatunnus_ei_kelpaa(self):
        virheviesti = repositories.kayttajat.luo_kayttaja(
            "ea", "PutinOnNilkki"
        )
        self.assertEqual(
            virheviesti, "Kayttäjätunnukset on oltava vähintään 4 merkkiä pitkä"
        )

    def test_liian_lyhyt_salasana_ei_kelpaa(self):
        virheviesti = repositories.kayttajat.luo_kayttaja(
            "Zelenskyi", "Putin"
        )
        self.assertEqual(
            virheviesti, "Salasanan on oltava vähintään 6 merkkiä pitkä"
        )

    def test_uuden_kayttajan_luonti_onnistuu(self):
        virheviesti = repositories.kayttajat.luo_kayttaja(
            "Zelenskyi", "PutinOnNilkki"
        )
        self.assertEqual(virheviesti, "")

    def test_voi_luoda_kayttajan_ja_logata_sisaan(self):
        repositories.kayttajat.luo_kayttaja(
            "Zelenskyi", "PutinOnNilkki"
        )
        self.assertTrue(repositories.kayttajat.login(
            "Zelenskyi", "PutinOnNilkki"
        ))

    def test_vaaralla_salasanalla_ei_paase(self):
        repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnNilkki")

        self.assertFalse(repositories.kayttajat.login(
            "Zelenskyi", "PutinOnKiva"
        ))

    def test_ei_voi_luoda_samaa_kayttajaa_kahdesti(self):
        repositories.kayttajat.luo_kayttaja(
            "Zelenskyi", "PutinOnNilkki"
        )
        virheviesti = repositories.kayttajat.luo_kayttaja(
            "Zelenskyi", "PutinOnKakka"
        )
        self.assertEqual(virheviesti, "Käyttäjätunnus on jo olemassa")

    def test_kirjautuminen_vaaralla_tunnuksella(self):
        self.assertFalse(
            repositories.kayttajat.login(
                "Putin", "PutininSalasana"
            )
        )
