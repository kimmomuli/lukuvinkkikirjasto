from flask import render_template, Blueprint, redirect, request, session, flash
from services.kayttaja_service import kayttaja_service

rekisteroityminen_bp = Blueprint("rekisteroityminen", __name__)


@rekisteroityminen_bp.route("/rekisteroityminen", methods=["GET", "POST"])
def rekisteroityminen():
    tunnus = ""
    if request.method == "POST":
        tunnus = request.form["tunnus"]
        salasana = request.form["salasana"]

        virhe = kayttaja_service.luo_kayttaja(tunnus, salasana)
        if not virhe:
            session["username"] = tunnus
            return redirect("/")
        flash(virhe, "virhe")

    return render_template("rekisteroityminen.html", tunnus=tunnus)
