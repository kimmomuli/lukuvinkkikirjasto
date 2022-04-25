import unittest
from services.book_tip_service import BookTipService


class StubTipRepository:
    def __init__(self):
        self.tips = []

    def add_book_tip(self, title: str, author: str, _: int, adder_username: str) -> bool:
        for tip in self.tips:
            if tip == (title, author, adder_username):
                return False
        self.tips.append((title, author, adder_username))
        return True


class TestBookTipService(unittest.TestCase):
    def setUp(self):
        self.book_tip_service = BookTipService(StubTipRepository())

    def test_adding_book_tip_with_valid_inputs(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "2000", "username")
        self.assertEqual(error, "")

    def test_adding_book_tip_with_a_year_that_is_a_decimal_number(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "1.5", "username")
        self.assertEqual(
            error, "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025")

    def test_adding_book_tip_with_a_year_that_is_a_string(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "year", "username")
        self.assertEqual(
            error, "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025")

    def test_adding_book_tip_with_too_short_title(self):
        error = self.book_tip_service.add_book_tip(
            "", "author", "2000", "username")
        self.assertEqual(error, "Otsikon tulee sisältää ainakin kaksi merkkiä")

    def test_adding_book_tip_with_too_short_author_name(self):
        error = self.book_tip_service.add_book_tip(
            "title", "", "2000", "username")
        self.assertEqual(
            error, "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä")

    def test_adding_book_tip_with_largest_allowed_year(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "2025", "username")
        self.assertEqual(error, "")

    def test_adding_book_tip_with_smallest_allowed_year(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "1", "username")
        self.assertEqual(error, "")

    def test_adding_book_tip_with_too_large_year(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "2026", "username")
        self.assertEqual(
            error, "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025")

    def test_adding_book_tip_with_too_small_year(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "0", "username")
        self.assertEqual(
            error, "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025")

    def test_adding_book_tip_with_negative_year(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "-1", "username")
        self.assertEqual(
            error, "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025")

    def test_adding_duplicate_book_tip(self):
        error = self.book_tip_service.add_book_tip(
            "title", "author", "2025", "username")
        self.assertEqual(error, "")
        error = self.book_tip_service.add_book_tip(
            "title", "author", "2025", "username")
        self.assertEqual(
            error, "Olet jo lisännyt kirjavinkin samalla otsikolla ja kirjailijalla")
