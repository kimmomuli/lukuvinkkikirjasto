from flask import render_template, Blueprint, redirect, request, session, flash
from services.kayttaja_service import kayttaja_service

kirjautuminen_bp = Blueprint("kirjautuminen", __name__)


@kirjautuminen_bp.route("/kirjautuminen", methods=["GET", "POST"])
def kirjautuminen():
    tunnus = ""
    if request.method == "POST":
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]
        virhe = kayttaja_service.kirjaudu_sisaan(tunnus, salasana)
        if not virhe:
            session["username"] = tunnus
            return redirect("/")
        flash(virhe, "virhe")

    return render_template("kirjautuminen.html", tunnus=tunnus)


@kirjautuminen_bp.route("/kirjaudu_ulos")
def kirjaudu_ulos():
    del session["username"]
    return redirect("/")
