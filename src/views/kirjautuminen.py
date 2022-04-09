from flask import render_template, Blueprint, redirect, request
from repositories.kayttajat import login, luo_kayttaja

kirjautuminen_bp = Blueprint("kirjautuminen", __name__)


@kirjautuminen_bp.route("/kirjautuminen")
def kirjautuminen():
    return render_template("kirjautuminen.html")


@kirjautuminen_bp.route("/rekisteroidu", methods=["POST"])
def rekisteroidu():
    try:
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]

        luo_kayttaja(tunnus, salasana)
        return redirect("/")
    except TypeError:
        return render_template("virhe.html")


@kirjautuminen_bp.route("/kirjaudu", methods=["POST"])
def kirjaudu():
    try:
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]
        if login(tunnus, salasana):
            return redirect("/")
        else:
            return redirect("/kirjautuminen")
    except TypeError:
        return render_template("virhe.html")
