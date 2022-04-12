import unittest
from repositories.vinkki_repositorio import vinkki_repositorio
from entities.kirjavinkki import Kirjavinkki


class TestVinkkiRepository(unittest.TestCase):
    def setUp(self):
        vinkki_repositorio.poista_kaikki()
        self.kirjavinkki1 = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy",
            "Fedor Dostojevski", 1880, "kayttaja")
        self.kirjavinkki2 = Kirjavinkki(
            "Anna Karenina", "Leo Tolstoi", 1878, "testaaja")

    def test_voi_tallettaa_kirjavinkin_ja_se_loytyy_kannasta(self):
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki1)
        vinkit = vinkki_repositorio.lataa_kirjat()
        self.assertEqual(vinkit[0].otsikko, self.kirjavinkki1.otsikko)

    def test_voi_tallettaa_useita_kirjavinkkeja(self):
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki1)
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki2)
        vinkit = vinkki_repositorio.lataa_kirjat()
        self.assertEqual(len(vinkit), 2)

    def test_kayttajan_tiedot_loytyvat_ladatulta_vinkilta(self):
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki1)
        vinkit = vinkki_repositorio.lataa_kirjat()
        self.assertEqual(vinkit[0].omistaja, self.kirjavinkki1.omistaja)

    def test_uusin_vinkki_ensimmaisena(self):
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki1)
        vinkki_repositorio.tallenna_kirjavinkki(self.kirjavinkki2)
        vinkit = vinkki_repositorio.lataa_kirjat()
        self.assertEqual(vinkit[0].otsikko, self.kirjavinkki2.otsikko)

    def test_kaksi_kayttajaa_voi_lisata_saman_kirjan(self):
        karamazov = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy", "Fedor Dostojevski", 1880, "kayttaja1")
        karamazov2 = Kirjavinkki(
            "Karamazovin veljekset - Bratja Karamazovy", "Fedor Dostojevski", 1880, "kayttaja2")
        vinkki_repositorio.tallenna_kirjavinkki(karamazov)
        vinkki_repositorio.tallenna_kirjavinkki(karamazov2)
        vinkit = vinkki_repositorio.lataa_kirjat()
        self.assertEqual(len(vinkit), 2)
