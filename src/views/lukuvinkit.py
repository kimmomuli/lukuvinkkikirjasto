from flask import render_template, Blueprint, redirect, request
from repositories.vinkit import lataa_kirjat, tallenna_kirjavinkki
from services.kirjavinkki_service import parse_kirjavinkki

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = lataa_kirjat()
    return render_template("lukuvinkit.html", vinkit=vinkit)


@lukuvinkit_bp.route("/uusi_vinkki")
def uusi_vinkki():
    return render_template("uusi_vinkki.html")


@lukuvinkit_bp.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    try:
        otsikko = request.form["otsikko"]
        kirjailija = request.form["kirjailija"]
        kirjoitusvuosi = request.form["kirjoitusvuosi"]
        omistaja = request.form["omistaja"]

        kirjavinkki = parse_kirjavinkki(
            otsikko, kirjailija, kirjoitusvuosi, omistaja
        )

        tallenna_kirjavinkki(kirjavinkki)
        return redirect("/")
    except TypeError:
        return render_template("virhe.html")
