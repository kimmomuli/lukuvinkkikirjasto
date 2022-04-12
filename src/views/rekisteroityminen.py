from flask import render_template, Blueprint, redirect, request, session, flash
from services.kayttaja_service import kayttaja_service

rekisteroityminen_bp = Blueprint("rekisteroityminen", __name__)


@rekisteroityminen_bp.route("/rekisteroityminen")
def rekisteroityminen():
    return render_template("rekisteroityminen.html")


@rekisteroityminen_bp.route("/rekisteroidu", methods=["POST"])
def rekisteroidu():
    tunnus = request.form["tunnus"]
    salasana = request.form["salasana"]

    virhe = kayttaja_service.luo_kayttaja(tunnus, salasana)
    if len(virhe) > 0:
        flash(virhe, "virhe")
        return redirect("/rekisteroityminen")
    session["username"] = tunnus
    return redirect("/")
