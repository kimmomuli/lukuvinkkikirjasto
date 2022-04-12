import unittest
from unittest.mock import Mock
from services.kirjavinkki_service import KirjavinkkiService


class KirjavinkkiServiceTest(unittest.TestCase):
    def setUp(self):
        self.vinkki_repositorio_mock = Mock()
        self.kirjavinkki_service = KirjavinkkiService(
            self.vinkki_repositorio_mock)

    def test_tarkista_kirjavinkki_oikealla_syotteella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2002", "kayttaja")
        self.assertEqual(virhe, "")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_called_once()

    def test_tarkista_kirjavinkki_kirjoitusvuodella_joka_on_desimaaliluku(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "1.5", "kayttaja")
        self.assertEqual(virhe, "Kirjoitusvuoden pitää olla numero")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()

    def test_tarkista_kirjavinkki_vaaralla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "vuosi", "kayttaja")
        self.assertEqual(virhe, "Kirjoitusvuoden pitää olla numero")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()

    def test_tarkista_kirjavinkki_liian_lyhyella_otsikolla(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "", "kirjailija", 2002, "kayttaja")
        self.assertEqual(virhe, "Otsikon tulee sisältää ainakin kaksi merkkiä")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()

    def test_tarkista_kirjavinkki_liian_lyhyella_kirjailijalla(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "", 2002, "kayttaja")
        self.assertEqual(
            virhe, "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()

    def test_tarkista_kirjavinkki_isoimmalla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2025", "kayttaja")
        self.assertEqual(virhe, "")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_called()

    def test_tarkista_kirjavinkki_pienimmällä_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "1", "kayttaja")
        self.assertEqual(virhe, "")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_called()

    def test_tarkista_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "2026", "kayttaja")
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()

    def test_tarkista_kirjavinkki_liian_isolla_kirjoitusvuodella(self):
        virhe = self.kirjavinkki_service.lisaa_kirjavinkki(
            "otsikko", "kirjailija", "0", "kayttaja")
        self.assertEqual(
            virhe, "Kirjoitusvuoden pitää olla numero väliltä 1-2025")
        self.vinkki_repositorio_mock.tallenna_kirjavinkki.assert_not_called()
