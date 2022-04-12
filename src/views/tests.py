from flask import Blueprint
from repositories.kayttaja_repositorio import kayttaja_repository
from repositories.vinkki_repositorio import vinkki_repositorio

tests_bp = Blueprint("test", __name__)


@tests_bp.route("/tests/reset", methods=["POST"])
def reset():
    kayttaja_repository.poista_kaikki()
    vinkki_repositorio.poista_kaikki()
    return "ok"
