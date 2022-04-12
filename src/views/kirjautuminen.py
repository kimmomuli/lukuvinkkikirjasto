from flask import render_template, Blueprint, redirect, request, session, flash
from repositories.kayttajat import kayttaja_repository

kirjautuminen_bp = Blueprint("kirjautuminen", __name__)


@kirjautuminen_bp.route("/kirjautuminen")
def kirjautuminen():
    return render_template("kirjautuminen.html")


@kirjautuminen_bp.route("/kirjaudu", methods=["POST"])
def kirjaudu():
    tunnus = request.form["tunnus"]
    salasana = request.form["salasana"]
    if kayttaja_repository.login(tunnus, salasana):
        session["username"] = tunnus
        return redirect("/")
    flash("Väärä käyttäjätunnus tai salasana", "virhe")
    return redirect("/kirjautuminen")


@kirjautuminen_bp.route("/kirjaudu_ulos")
def kirjaudu_ulos():
    del session["username"]
    return redirect("/")
