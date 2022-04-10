from flask import render_template, Blueprint, redirect, request, session, flash
from repositories.vinkit import tallenna_kirjavinkki
from services.kirjavinkki_service import parse_kirjavinkki, tarkista_kirjavinkki

uusi_lukuvinkki_bp = Blueprint("uusi_lukuvinkki", __name__)


@uusi_lukuvinkki_bp.route("/uusi_vinkki")
def uusi_vinkki():
    return render_template("uusi_vinkki.html")


@uusi_lukuvinkki_bp.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    virheet = []
    try:
        otsikko = request.form["otsikko"]
        #if type(otsikko) != str:
        #    virhe = "Otsikon pitää sisältää kirjaimia"t
        kirjailija = request.form["kirjailija"]
        kirjoitusvuosi = request.form["kirjoitusvuosi"]
        omistaja = session["username"]
        virheet = tarkista_kirjavinkki(otsikko, kirjailija, kirjoitusvuosi)
        if not virheet:
            kirjavinkki = parse_kirjavinkki(
                otsikko, kirjailija, kirjoitusvuosi, omistaja
            )
            tallenna_kirjavinkki(kirjavinkki)
            return redirect("/")
        for virhe in virheet:
            flash(virhe, "virhe")
        return render_template("uusi_vinkki.html")
    except TypeError:
        return render_template("virhe.html")
