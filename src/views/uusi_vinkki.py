from flask import render_template, Blueprint, redirect, request, session
from repositories.vinkit import tallenna_kirjavinkki
from services.kirjavinkki_service import parse_kirjavinkki

uusi_lukuvinkki_bp = Blueprint("uusi_lukuvinkki", __name__)


@uusi_lukuvinkki_bp.route("/uusi_vinkki")
def uusi_vinkki():
    return render_template("uusi_vinkki.html")


@uusi_lukuvinkki_bp.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    try:
        otsikko = request.form["otsikko"]
        kirjailija = request.form["kirjailija"]
        kirjoitusvuosi = request.form["kirjoitusvuosi"]
        omistaja = session["username"]

        kirjavinkki = parse_kirjavinkki(
            otsikko, kirjailija, kirjoitusvuosi, omistaja
        )

        tallenna_kirjavinkki(kirjavinkki)
        return redirect("/")
    except TypeError:
        return render_template("virhe.html")
