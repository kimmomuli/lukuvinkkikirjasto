import unittest
from entities.kirjavinkki import Kirjavinkki
from services.kirjavinkki_service import KirjavinkkiService


class StubVinkkiRepositorio:
    def __init__(self):
        self.vinkit = []

    def tallenna_kirjavinkki(self, kirjavinkki: Kirjavinkki) -> bool:
        for vinkki in self.vinkit:
            if vinkki == (kirjavinkki.otsikko, kirjavinkki.omistaja):
                return False
        self.vinkit.append((kirjavinkki.otsikko, kirjavinkki.omistaja))
        return True


class KirjavinkkiServiceTest(unittest.TestCase):
    def setUp(self):
        self.kirjavinkki_service = KirjavinkkiService(StubVinkkiRepositorio())

    def test_lisaa_kirjavinkki_oikealla_syotteella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2002", "kayttaja")
        self.assertEqual(virhe, "")

    def test_lisaa_kirjavinkki_kirjoitusvuodella_joka_on_desimaaliluku(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "1.5", "kayttaja")
        self.assertEqual(virhe, "Kirjoitusvuoden pitää olla numero")

    def test_lisaa_kirjavinkki_vaaralla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "vuosi", "kayttaja")
        self.assertEqual(virhe, "Kirjoitusvuoden pitää olla numero")

    def test_lisaa_kirjavinkki_liian_lyhyella_otsikolla(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "", "kirjailija", 2002, "kayttaja")
        self.assertEqual(virhe, "Otsikon tulee sisältää ainakin kaksi merkkiä")

    def test_lisaa_kirjavinkki_liian_lyhyella_kirjailijalla(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "", 2002, "kayttaja")
        self.assertEqual(
            virhe, "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä")

    def test_lisaa_kirjavinkki_isoimmalla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2025", "kayttaja")
        self.assertEqual(virhe, "")

    def test_lisaa_kirjavinkki_pienimmällä_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "1", "kayttaja")
        self.assertEqual(virhe, "")

    def test_lisaa_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2026", "kayttaja")
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")

    def test_lisaa_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "0", "kayttaja")
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")

    def test_lisaa_duplikaatti_kirjavinkki(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2025", "kayttaja")
        self.assertEqual(virhe, "")
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2025", "kayttaja")
        self.assertEqual(
            virhe, "Olet jo lisännyt kirjavinkin samalla otsikolla")
