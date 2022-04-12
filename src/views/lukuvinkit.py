from flask import render_template, Blueprint
from repositories.vinkki_repositorio import vinkki_repositorio

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = vinkki_repositorio.lataa_kirjat()
    return render_template("lukuvinkit.html", vinkit=vinkit)
