import unittest
from services.kirjavinkki_service import kirjavinkki_service


class ServiceTest(unittest.TestCase):
    def test_tarkista_kirjavinkki_oikealla_syotteella(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki(
            "otsikko", "kirjailija", 2002)
        self.assertEqual(virhe, "")

    def test_tarkista_kirjavinkki_vaaralla_kirjoitusvuodella(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki(
            "otsikko", "kirjailija", "vuosi")
        self.assertEqual(virhe, "Kirjoitusvuoden pitää olla numero")

    def test_tarkista_kirjavinkki_liian_lyhyella_otsikolla(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki(
            "", "kirjailija", 2002)
        self.assertEqual(virhe, "Otsikon tulee sisältää ainakin kaksi merkkiä")

    def test_tarkista_kirjavinkki_liian_lyhyella_kirjailijalla(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki("otsikko", "", 2002)
        self.assertEqual(
            virhe, "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä")

    def test_tarkista_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki(
            "otsikko", "kirjailija", 2026)
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")

    def test_tarkista_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = kirjavinkki_service.tarkista_kirjavinkki(
            "otsikko", "kirjailija", 0)
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")
