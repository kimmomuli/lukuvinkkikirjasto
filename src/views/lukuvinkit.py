from flask import render_template, Blueprint
from entities.kirjavinkki import Kirjavinkki

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = [
        Kirjavinkki("testiotsikko", "testikirjailija", "1970", "testaaja"),
        Kirjavinkki("testiotsikko2")
    ]
    return render_template("lukuvinkit.html", vinkit=vinkit)
