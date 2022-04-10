from flask import render_template, Blueprint, redirect, session
from repositories.vinkit import lataa_kirjat

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = lataa_kirjat()
    error=None
    return render_template("lukuvinkit.html", vinkit=vinkit, error=error)


@lukuvinkit_bp.route("/kirjaudu_ulos")
def kirjaudu_ulos():
    session["username"] = ""
    return redirect("/")
