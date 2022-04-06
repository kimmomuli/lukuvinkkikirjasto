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
        virheviesti = ""
        try:
            repositories.kayttajat.luo_kayttaja("ea", "PutinOnNilkki")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertEqual(
            virheviesti, "Kayttäjätunnukset on oltava vähintään 6 merkkiä pitkä")

    def test_liian_lyhyt_salasana_ei_kelpaa(self):
        virheviesti = ""
        try:
            repositories.kayttajat.luo_kayttaja("Zelenskyi", "Putin")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertEqual(
            virheviesti, "Salasanan on oltava vähintään 6 merkkiä pitkä")

    def test_uuden_kayttajan_luonti_onnistuu(self):
        virheviesti = "tyhja"
        try:
            repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertEqual(virheviesti, "tyhja")

    def test_voi_luoda_kayttajan_ja_logata_sisaan(self):
        virheviesti = "tyhja"
        try:
            repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertTrue(repositories.kayttajat.login(
            "Zelenskyi", "PutinOnNilkki"))

    def test_vaaralla_salasanalla_ei_paase(self):
        virheviesti = "tyhja"
        try:
            repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertFalse(repositories.kayttajat.login(
            "Zelenskyi", "PutinOnKiva"))

    def test_ei_voi_luoda_samaa_kayttajaa_kahdesti(self):
        virheviesti = ""
        repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnNilkki")
        try:
            repositories.kayttajat.luo_kayttaja("Zelenskyi", "PutinOnKakka")
        except Exception as e:
            virheviesti = e.args[0]
        self.assertEqual(virheviesti, "Käyttäjätunnus on jo olemassa")
