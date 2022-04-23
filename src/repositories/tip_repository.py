from typing import List
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation  # pylint: disable=no-name-in-module
from database import database
from entities.book_tip import BookTip


class TipRepository:
    def get_all_book_tips(self) -> List[BookTip]:
        sql = """SELECT bt.title, bt.author, bt.year, t.timestamp, t.adder_username
                 FROM book_tips bt INNER JOIN tips t ON bt.title = t.title AND bt.author = t.author
                 ORDER BY timestamp DESC"""
        result = database.session.execute(sql)
        tips = result.fetchall()
        book_tips = []
        for tip in tips:
            book_tips.append(BookTip(
                tip["title"], tip["author"], tip["year"], tip["adder_username"], tip["timestamp"], self.get_tip_likes(
                    "Book", tip["title"], tip["author"])
            ))

        return book_tips

    def get_tip_likes(self, tip_type: str, title: str, author: str) -> List[str]:
        sql = "SELECT username FROM likes WHERE type = :type AND title = :title AND author = :author"

        result = database.session.execute(sql,
                                          {
                                              "type": tip_type,
                                              "title": title,
                                              "author": author
                                          }
                                          ).fetchall()
        all_likes = []
        for item in result:
            all_likes.append(item["username"])
        return all_likes

    def add_book_tip(self, book_tip: BookTip) -> bool:
        try:
            sql = """INSERT INTO tips (type, title, author, adder_username, timestamp)
                     VALUES (:type, :title, :author, :adder_username, :timestamp)"""
            database.session.execute(
                sql,
                {
                    "type": book_tip.type,
                    "title": book_tip.title,
                    "author": book_tip.author,
                    "adder_username": book_tip.adder_username,
                    "timestamp": datetime.now()
                }
            )

            sql2 = """INSERT INTO book_tips (title, author, year)
                      VALUES (:title, :author, :year) 
                      ON CONFLICT DO NOTHING"""
            database.session.execute(
                sql2,
                {
                    "title": book_tip.title,
                    "author": book_tip.author,
                    "year": book_tip.year
                }
            )
            database.session.commit()
            return True
        except IntegrityError as error:
            # UNIQUE constraint fail
            assert isinstance(error.orig, UniqueViolation)
            database.session.rollback()
            return False

    def add_like(self, tip: BookTip, username: str) -> None:

        sql = """INSERT INTO likes VALUES (:type, :title, :author, :username)"""
        database.session.execute(sql,
                                 {
                                     "type": 'Book',
                                     "title": tip.title,
                                     "author": tip.author,
                                     "username": username
                                 })
        database.session.commit()

    def delete_tip_like(self, tip: BookTip, username: str) -> None:
        sql = "DELETE FROM likes WHERE type = :type AND title = :title AND author = :author AND username = :username"

        database.session.execute(sql, {
            "type": tip.type,
            "title": tip.title,
            "author": tip.author,
            "username": username
        })

    def delete_all(self) -> None:
        sql = "DELETE FROM tips; DELETE FROM book_tips; DELETE FROM likes"
        database.session.execute(sql)
        database.session.commit()

    def delete_tip(self, tip: BookTip) -> None:
        sql = """DELETE FROM tips
                 WHERE type = :type AND title = :title AND adder_username = :adder_username"""
        database.session.execute(
            sql, {"type": tip.type, "title": tip.title, "adder_username": tip.adder_username})
        database.session.commit()


tip_repository = TipRepository()
