from flask import render_template, Blueprint
from repositories.vinkit import vinkki_repositorio

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = vinkki_repositorio.lataa_kirjat()
    error = None
    return render_template("lukuvinkit.html", vinkit=vinkit, error=error)
