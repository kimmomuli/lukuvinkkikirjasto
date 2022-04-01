import unittest
import repositories.vinkit
from entities.kirjavinkki import Kirjavinkki


class TestVinkit(unittest.TestCase):
    def setUp(self):
        pass

    def test_voi_tallettaa_kirjavinkin_ja_se_loytyy_kannasta(self):
        karamazov = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy", "Fedor Dostojevski", 1880)
        repositories.vinkit.tallenna_kirjavinkki(karamazov)
        vinkit = repositories.vinkit.lataa_kirjat()
        self.assertEqual(vinkit[0].otsikko, karamazov.otsikko)

    def test_voi_tallettaa_useita_kirjavinkkeja(self):
        pass
