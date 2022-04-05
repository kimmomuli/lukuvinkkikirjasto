from flask import render_template, Blueprint
from repositories.vinkit import lataa_kirjat

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = lataa_kirjat()
    return render_template("lukuvinkit.html", vinkit=vinkit)
