from repositories.tip_repository import TipRepository
from repositories.tip_repository import tip_repository as default_tip_repository


class BookTipService:
    def __init__(self, tip_repository: TipRepository = default_tip_repository) -> None:
        self._tip_repositorio = tip_repository

    def add_book_tip(self, title: str, author: str, year: str, adder_username: str) -> str:
        if len(title) < 2:
            return "Otsikon tulee sisältää ainakin kaksi merkkiä"
        if len(author) < 2:
            return "Kirjailijan nimen tulee sisältää ainakin kaksi merkkiä"
        if not str.isdigit(year) or not 1 <= int(year) <= 2025:
            return "Kirjoitusvuoden pitää olla kokonaisluku väliltä 1-2025"

        result = self._tip_repositorio.add_book_tip(
            title, author, year, adder_username)
        if not result:
            return "Olet jo lisännyt kirjavinkin samalla otsikolla ja kirjailijalla"
        return ""


book_tip_service = BookTipService()
