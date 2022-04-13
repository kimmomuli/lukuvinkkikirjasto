# pylint: disable=invalid-name
import requests


class AppLibrary:
    def __init__(self) -> None:
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self) -> None:
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, username: str, password: str) -> None:
        data = {
            "username": username,
            "password": password,
        }

        requests.post(f"{self._base_url}/register", data=data)

    def add_book_tip(self, title: str, author: str, year: str, adder_username: str) -> None:
        data = {
            "title": title,
            "author": author,
            "year": year,
            "adder_username": adder_username
        }

        requests.post(f"{self._base_url}/tests/add_book_tip", json=data)
