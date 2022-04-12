from flask import render_template, Blueprint, redirect, request, session, flash
from services.kirjavinkki_service import kirjavinkki_service

uusi_lukuvinkki_bp = Blueprint("uusi_lukuvinkki", __name__)


@uusi_lukuvinkki_bp.route("/uusi_vinkki", methods=["GET", "POST"])
def uusi_vinkki():
    otsikko = ""
    kirjailija = ""
    kirjoitusvuosi = ""
    if request.method == "POST":
        otsikko = request.form["otsikko"]
        kirjailija = request.form["kirjailija"]
        kirjoitusvuosi = request.form["kirjoitusvuosi"]
        omistaja = session["username"]

        virhe = kirjavinkki_service.lisaa_kirjavinkki(
            otsikko, kirjailija, kirjoitusvuosi, omistaja)

        if not virhe:
            return redirect("/")
        flash(virhe, "virhe")

    return render_template(
        "uusi_vinkki.html",
        otsikko=otsikko,
        kirjailija=kirjailija,
        kirjoitusvuosi=kirjoitusvuosi
    )
