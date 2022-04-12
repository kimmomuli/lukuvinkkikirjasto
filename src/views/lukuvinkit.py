from flask import render_template, Blueprint, request, session
from repositories.vinkki_repositorio import vinkki_repositorio

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/", methods=["GET", "POST"])
def lukuvinkit():
    vinkit = vinkki_repositorio.lataa_kirjat()
    if request.method == "POST":
        for vinkki in vinkit:
            if (request.form.get(f"delete_{vinkki.tyyppi}_{vinkki.otsikko}")
                    and vinkki.omistaja == session["username"]):
                vinkki_repositorio.poista_vinkki(vinkki)
        vinkit = vinkki_repositorio.lataa_kirjat()
    return render_template("lukuvinkit.html", vinkit=vinkit)
