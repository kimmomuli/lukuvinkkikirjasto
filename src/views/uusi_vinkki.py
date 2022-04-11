from flask import render_template, Blueprint, redirect, request, session, flash
from repositories.vinkit import tallenna_kirjavinkki
from services.kirjavinkki_service import tarkista_kirjavinkki
from entities.kirjavinkki import Kirjavinkki

uusi_lukuvinkki_bp = Blueprint("uusi_lukuvinkki", __name__)


@uusi_lukuvinkki_bp.route("/uusi_vinkki")
def uusi_vinkki():
    return render_template("uusi_vinkki.html")


@uusi_lukuvinkki_bp.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():

    otsikko = request.form["otsikko"]
    kirjailija = request.form["kirjailija"]
    kirjoitusvuosi = request.form["kirjoitusvuosi"]
    omistaja = session["username"]

    virhe = tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi)

    if len(virhe) > 0:
        flash(virhe, "virhe")
        return render_template("uusi_vinkki.html")

    kirjavinkki = Kirjavinkki(
        otsikko, kirjailija, kirjoitusvuosi, omistaja
    )

    tallenna_kirjavinkki(kirjavinkki)

    return redirect("/")
