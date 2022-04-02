import flask_testing
from flask import Flask
import repositories.vinkit
from initialize_database import initialize_database
from app import create_app
from entities.kirjavinkki import Kirjavinkki


class TestVinkit(flask_testing.TestCase):
    def create_app(self):
        return create_app(testing=True)

    def setUp(self):
        initialize_database()

    def test_voi_tallettaa_kirjavinkin_ja_se_loytyy_kannasta(self):
        karamazov = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy", "Fedor Dostojevski", 1880)
        repositories.vinkit.tallenna_kirjavinkki(karamazov)
        vinkit = repositories.vinkit.lataa_kirjat()
        self.assertEqual(vinkit[0].otsikko, karamazov.otsikko)

    def test_voi_tallettaa_useita_kirjavinkkeja(self):
        karamazov = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy", "Fedor Dostojevski", 1880)
        repositories.vinkit.tallenna_kirjavinkki(karamazov)
        anna = Kirjavinkki("Anna Karenina", "Leo Tolstoi", 1878, "testaaja ")
        repositories.vinkit.tallenna_kirjavinkki(anna)
        vinkit = repositories.vinkit.lataa_kirjat()
        self.assertEqual(len(vinkit), 2)
