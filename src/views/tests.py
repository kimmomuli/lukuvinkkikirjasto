from flask import Blueprint, request
from repositories.kayttaja_repositorio import kayttaja_repository
from repositories.vinkki_repositorio import vinkki_repositorio
from services.kirjavinkki_service import kirjavinkki_service

tests_bp = Blueprint("test", __name__)


@tests_bp.route("/tests/reset", methods=["POST"])
def reset():
    kayttaja_repository.poista_kaikki()
    vinkki_repositorio.poista_kaikki()
    return "ok"


@tests_bp.route("/tests/lisaa_kirjavinkki", methods=["POST"])
def lisaa_kirjavinkki():
    otsikko = request.json["otsikko"]
    kirjailija = request.json["kirjailija"]
    kirjoitusvuosi = request.json["kirjoitusvuosi"]
    omistaja = request.json["omistaja"]
    kirjavinkki_service.lisaa_kirjavinkki(
        otsikko, kirjailija, kirjoitusvuosi, omistaja)
    return "ok"
