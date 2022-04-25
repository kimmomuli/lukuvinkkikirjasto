from typing import List
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation  # pylint: disable=no-name-in-module
from database import database
from entities.book_tip import BookTip


class TipRepository:
    def get_all_tips(self) -> List[BookTip]:
        sql = """SELECT t.id, t.type, t.title, t.author, t.timestamp, t.adder_username
                 FROM tips t LEFT JOIN likes l ON l.tip_id = t.id
                 GROUP BY t.id
                 ORDER BY COUNT(l.username) DESC, t.timestamp DESC"""

        result = database.session.execute(sql)
        tips = []
        for tip in result.fetchall():
            if tip["type"] == "book":
                tips.append(self.get_book_tip(
                    tip["id"],
                    tip["title"],
                    tip["author"],
                    tip["adder_username"],
                    tip["timestamp"],
                    self.get_tip_likes(tip["id"])
                ))

        return tips

    def get_book_tip(self, tip_id: int, title: str, author: str, adder_username: str, timestamp: datetime, likes: List[str]) -> BookTip:
        sql = """SELECT title, author, year
                 FROM book_tips
                 WHERE title = :title AND author = :author"""
        book_tip = database.session.execute(sql, {
            "title": title,
            "author": author
        }).fetchone()

        return BookTip(
            tip_id,
            book_tip["title"],
            book_tip["author"],
            book_tip["year"],
            adder_username,
            timestamp,
            likes
        )

    def get_tip_likes(self, tip_id: int) -> List[str]:
        sql = "SELECT username FROM likes WHERE tip_id = :tip_id"

        result = database.session.execute(sql, {"tip_id": tip_id}).fetchall()
        all_likes = []
        for item in result:
            all_likes.append(item["username"])
        return all_likes

    def get_tip_id(self, tip: BookTip) -> int:
        sql = """SELECT id
                 FROM tips
                 WHERE type = :type AND title = :title AND author = :author AND adder_username = :adder_username"""
        result = database.session.execute(sql, {
            "type": tip.type,
            "title": tip.title,
            "author": tip.author,
            "adder_username": tip.adder_username
        }).fetchone()
        return int(result["id"])

    def add_book_tip(self, title: str, author: str, year: int, adder_username: str) -> bool:
        try:
            sql = """INSERT INTO tips (type, title, author, adder_username, timestamp)
                     VALUES (:type, :title, :author, :adder_username, :timestamp)"""
            database.session.execute(
                sql,
                {
                    "type": "book",
                    "title": title,
                    "author": author,
                    "adder_username": adder_username,
                    "timestamp": datetime.now()
                }
            )

            sql2 = """INSERT INTO book_tips (title, author, year)
                      VALUES (:title, :author, :year) 
                      ON CONFLICT DO NOTHING"""
            database.session.execute(sql2, {
                "title": title,
                "author": author,
                "year": year
            })
            database.session.commit()
            return True
        except IntegrityError as error:
            # UNIQUE constraint fail
            assert isinstance(error.orig, UniqueViolation)
            database.session.rollback()
            return False

    def add_like(self, tip_id: int, username: str) -> bool:
        try:
            sql = """INSERT INTO likes VALUES (:tip_id, :username)"""
            database.session.execute(sql, {
                "tip_id": tip_id,
                "username": username
            })
            database.session.commit()
            return True
        except IntegrityError as error:
            # UNIQUE constraint fail
            assert isinstance(error.orig, UniqueViolation)
            database.session.rollback()
            return False

    def remove_like(self, tip_id: int, username: str) -> bool:
        sql = "DELETE FROM likes WHERE tip_id = :tip_id AND username = :username"

        database.session.execute(sql, {
            "tip_id": tip_id,
            "username": username
        })
        database.session.commit()
        # I'm pretty sure this cannot fail so just return True :D.
        return True

    def delete_all(self) -> None:
        sql = "DELETE FROM likes; DELETE FROM tips; DELETE FROM book_tips"
        database.session.execute(sql)
        database.session.commit()

    def delete_tip(self, tip: BookTip) -> None:
        sql = """DELETE FROM tips
                 WHERE type = :type AND title = :title AND adder_username = :adder_username"""
        database.session.execute(
            sql, {"type": tip.type, "title": tip.title, "adder_username": tip.adder_username})
        database.session.commit()


tip_repository = TipRepository()
