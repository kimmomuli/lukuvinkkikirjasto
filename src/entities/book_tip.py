from typing import Optional, List


class BookTip:
    def __init__(self, tip_id: int, title: str, author: str, year: int,  # pylint: disable=too-many-arguments
                 adder_username: str, timestamp: Optional[str] = None, likes: Optional[List[str]] = None) -> None:
        self.id = tip_id
        self.title = title
        self.author = author
        self.year = year
        self.adder_username = adder_username
        self.type = "book"
        self.timestamp = timestamp
        self.likes = likes if likes else []

    def __eq__(self, other: "BookTip") -> bool:
        return (self.title == other.title
                and self.author == other.author
                and self.year == other.year
                and self.adder_username == other.adder_username
                and self.type == other.type
                and self.likes == other.likes)

    def __hash__(self):
        likes_hash = 0
        for like in self.likes:
            likes_hash += hash(like)
        return hash((self.title, self.author, self.year, self.adder_username, self.type, likes_hash))
