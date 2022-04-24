import unittest
from repositories.tip_repository import tip_repository
from entities.book_tip import BookTip


class TestTipRepository(unittest.TestCase):
    def setUp(self):
        tip_repository.delete_all()
        self.book_tip1 = BookTip("title1", "author1", 2000, "username1")
        self.book_tip2 = BookTip("title2", "author2", 1700, "username2")

    def test_after_adding_book_tip_it_is_saved_to_database(self):
        tip_repository.add_book_tip(self.book_tip1)
        tips = tip_repository.get_all_book_tips()
        self.assertEqual(tips[0], self.book_tip1)

    def test_adding_multiple_book_tips(self):
        tip_repository.add_book_tip(self.book_tip1)
        tip_repository.add_book_tip(self.book_tip2)
        tips = tip_repository.get_all_book_tips()
        self.assertCountEqual(tips, [self.book_tip1, self.book_tip2])

    def test_adding_same_tip_multiple_times_fails(self):
        result = tip_repository.add_book_tip(self.book_tip1)
        self.assertTrue(result)
        result = tip_repository.add_book_tip(self.book_tip1)
        self.assertFalse(result)

    def test_the_newest_tip_is_first(self):
        tip_repository.add_book_tip(self.book_tip1)
        tip_repository.add_book_tip(self.book_tip2)
        tips = tip_repository.get_all_book_tips()
        self.assertEqual(tips[0], self.book_tip2)

    def test_two_users_can_add_the_same_book_tip(self):
        book_tip1 = BookTip("title", "author", 1880, "username1")
        book_tip2 = BookTip("title", "author", 1880, "username2")
        tip_repository.add_book_tip(book_tip1)
        tip_repository.add_book_tip(book_tip2)
        tips = tip_repository.get_all_book_tips()
        self.assertCountEqual(tips, [book_tip1, book_tip2])

    def test_deleting_tip(self):
        tip_repository.add_book_tip(self.book_tip1)
        tip_repository.add_book_tip(self.book_tip2)
        tip_repository.delete_tip(self.book_tip1)
        tips = tip_repository.get_all_book_tips()
        self.assertCountEqual(tips, [self.book_tip2])

    def test_deleting_nonexistent_tip(self):
        tip_repository.add_book_tip(self.book_tip1)
        tip_repository.delete_tip(self.book_tip2)
        tips = tip_repository.get_all_book_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_like_can_be_added_to_tip(self):
        gulag = BookTip("Gulag vankileirien saaristo",
                        "Alexander Solzenitsyn", 1968, "Trotsky")

        tip_repository.add_book_tip(gulag)

        tip_repository.add_like(gulag.title, gulag.author, "JStalin")
        tips = tip_repository.get_all_book_tips()
        self.assertEqual(tips[0].likes[0], "JStalin")

    def test_two_users_can_like_same_book(self):
        gulag = BookTip("Gulag vankileirien saaristo",
                        "Alexander Solzenitsyn", 1968, "Trotsky")

        tip_repository.add_book_tip(gulag)

        tip_repository.add_like(gulag.title, gulag.author, "JStalin")
        tip_repository.add_like(gulag.title, gulag.author, "ILenin")
        tips = tip_repository.get_all_book_tips()
        self.assertEqual(tips[0].likes, ["ILenin", "JStalin"])

    def test_user_can_dislike_liked_booktip(self):
        anna = BookTip("Anna Karenina",
                       "Leo Tolstoi", 1878, "LTrotsky")

        tip_repository.add_book_tip(anna)

        tip_repository.add_like(anna.title, anna.author, "JStalin")
        tip_repository.add_like(anna.title, anna.author, "ILenin")
        tip_repository.remove_like(anna.title, anna.author, "JStalin")
        tips = tip_repository.get_all_book_tips()
        self.assertEqual(tips[0].likes[0], "ILenin")
