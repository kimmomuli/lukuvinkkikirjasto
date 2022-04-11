from flask import render_template, Blueprint, redirect, request, session, flash
from repositories.kayttajat import login, luo_kayttaja

rekisteroityminen_bp = Blueprint("rekisteroityminen", __name__)


@rekisteroityminen_bp.route("/rekisteroityminen")
def rekisteroityminen():
    return render_template("rekisteroityminen.html")


@rekisteroityminen_bp.route("/rekisteroidu", methods=["POST"])
def rekisteroidu():
    tunnus = request.form["tunnus"]
    salasana = request.form["salasana"]

    virhe = luo_kayttaja(tunnus, salasana)
    if len(virhe) > 0:
        flash(virhe, "virhe")
        return redirect("/rekisteroityminen")
    session["username"] = tunnus
    return redirect("/")
