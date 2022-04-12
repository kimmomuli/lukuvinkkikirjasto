from flask import render_template, Blueprint, redirect, request, session, flash
from services.kayttaja_service import kayttaja_service

kirjautuminen_bp = Blueprint("kirjautuminen", __name__)


@kirjautuminen_bp.route("/kirjautuminen")
def kirjautuminen():
    return render_template("kirjautuminen.html")


@kirjautuminen_bp.route("/kirjaudu", methods=["POST"])
def kirjaudu():
    tunnus = request.form["tunnus"]
    salasana = request.form["salasana"]
    virhe = kayttaja_service.kirjaudu_sisaan(tunnus, salasana)
    if virhe:
        flash(virhe, "virhe")
        return redirect("/kirjautuminen")
    session["username"] = tunnus
    return redirect("/")


@kirjautuminen_bp.route("/kirjaudu_ulos")
def kirjaudu_ulos():
    del session["username"]
    return redirect("/")
