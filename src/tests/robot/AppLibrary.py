# pylint: disable=invalid-name
import requests


class AppLibrary:
    def __init__(self) -> None:
        self._base_url = "http://localhost:5000"
        self.reset_application()

    def reset_application(self) -> None:
        requests.post(f"{self._base_url}/tests/reset")

    def create_user(self, kayttajatunnus: str, salasana: str) -> None:
        data = {
            "tunnus": kayttajatunnus,
            "salasana": salasana,
        }

        requests.post(f"{self._base_url}/rekisteroityminen", data=data)
