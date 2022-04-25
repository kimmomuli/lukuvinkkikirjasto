import unittest
from repositories.tip_repository import tip_repository
from entities.book_tip import BookTip


class TestTipRepository(unittest.TestCase):
    def setUp(self):
        tip_repository.delete_all()
        self.book_tip1 = BookTip(1, "title1", "author1", 2000, "username1")
        self.book_tip2 = BookTip(2, "title2", "author2", 1700, "username2")

    def _add_book_tip(self, book_tip: BookTip, correct_result: bool = True) -> bool:
        result = tip_repository.add_book_tip(
            book_tip.title, book_tip.author, book_tip.year, book_tip.adder_username)
        self.assertEqual(result, correct_result)

        book_tip.id = tip_repository.get_tip_id(book_tip)

    def test_after_adding_book_tip_it_is_saved_to_database(self):
        self._add_book_tip(self.book_tip1)

        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_adding_multiple_book_tips(self):
        self._add_book_tip(self.book_tip1)
        self._add_book_tip(self.book_tip2)

        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1, self.book_tip2])

    def test_adding_same_tip_multiple_times_fails(self):
        self._add_book_tip(self.book_tip1)
        self._add_book_tip(self.book_tip1, False)

    def test_the_sorting_tips(self):
        self._add_book_tip(self.book_tip1)
        self._add_book_tip(self.book_tip2)
        tip_repository.add_like(self.book_tip1.id, "JStalin")

        self.book_tip1.likes.append("JStalin")

        tips = tip_repository.get_all_tips()
        self.assertEqual(tips[0], self.book_tip1)

        tips = tip_repository.get_all_tips(order="time")
        self.assertEqual(tips[0], self.book_tip2)

    def test_two_users_can_add_the_same_book_tip(self):
        book_tip1 = BookTip(1, "title", "author", 1880, "username1")
        book_tip2 = BookTip(2, "title", "author", 1880, "username2")
        self._add_book_tip(book_tip1)
        self._add_book_tip(book_tip2)

        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [book_tip1, book_tip2])

    def test_deleting_tip(self):
        self._add_book_tip(self.book_tip1)
        self._add_book_tip(self.book_tip2)
        tip_repository.delete_tip(self.book_tip1)

        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip2])

    def test_deleting_nonexistent_tip(self):
        self._add_book_tip(self.book_tip1)
        tip_repository.delete_tip(self.book_tip2)

        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_like_can_be_added_to_tip(self):
        self._add_book_tip(self.book_tip1)
        tip_repository.add_like(self.book_tip1.id, "JStalin")

        self.book_tip1.likes.append("JStalin")
        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_same_user_cannot_like_same_tip_twice(self):
        self._add_book_tip(self.book_tip1)

        result = tip_repository.add_like(self.book_tip1.id, "JStalin")
        self.assertTrue(result)
        result = tip_repository.add_like(self.book_tip1.id, "JStalin")
        self.assertFalse(result)

        self.book_tip1.likes.append("JStalin")
        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_two_users_can_like_same_book(self):
        self._add_book_tip(self.book_tip1)
        tip_repository.add_like(self.book_tip1.id, "JStalin")
        tip_repository.add_like(self.book_tip1.id, "ILenin")

        self.book_tip1.likes.append("JStalin")
        self.book_tip1.likes.append("ILenin")
        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])

    def test_user_can_remove_like(self):
        self._add_book_tip(self.book_tip1)

        tip_repository.add_like(self.book_tip1.id, "JStalin")
        tip_repository.add_like(self.book_tip1.id, "ILenin")
        tip_repository.remove_like(self.book_tip1.id, "JStalin")

        self.book_tip1.likes.append("ILenin")
        tips = tip_repository.get_all_tips()
        self.assertCountEqual(tips, [self.book_tip1])
