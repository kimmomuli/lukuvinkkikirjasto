from typing import Optional


class BookTip:
    def __init__(self, title: str, author: str, year: int,
                 adder_username: str, timestamp: Optional[str] = None, likes=[]) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.adder_username = adder_username
        self.type = "book"
        self.timestamp = timestamp
        self.likes = likes

    def __eq__(self, other: "BookTip") -> bool:
        return (self.title == other.title
                and self.author == other.author
                and self.year == other.year
                and self.adder_username == other.adder_username
                and self.type == other.type)

    def __hash__(self):
        return hash((self.title, self.author, self.year, self.adder_username, self.type))
