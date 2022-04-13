from repositories.user_repository import UserRepository
from repositories.user_repository import user_repository as default_user_repository


class UserService:
    def __init__(self, user_repository: UserRepository = default_user_repository) -> None:
        self._user_repository = user_repository

    def register(self, username: str, password: str) -> str:
        if self._user_repository.user_exists(username):
            return "Käyttäjätunnus on jo olemassa"
        if len(password) < 6:
            return "Salasanan on oltava vähintään 6 merkkiä pitkä"
        if len(username) < 4:
            return "Kayttäjätunnuksen on oltava vähintään 4 merkkiä pitkä"

        self._user_repository.add_user(username, password)
        return ""

    def log_in(self, username: str, password: str) -> str:
        result = self._user_repository.log_in(username, password)
        if not result:
            return "Väärä käyttäjätunnus tai salasana"
        return ""


user_service = UserService()
