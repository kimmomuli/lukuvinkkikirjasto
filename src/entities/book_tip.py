from typing import Optional


class BookTip:
    def __init__(self, title: str, author: str, year: int,
                 adder_username: str, timestamp: Optional[str] = None) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.adder_username = adder_username
        self.type = "book"
        self.timestamp = timestamp
