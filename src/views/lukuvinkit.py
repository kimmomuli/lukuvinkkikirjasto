from flask import render_template, Blueprint
from entities.kirjavinkki import kirjavinkki

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)


@lukuvinkit_bp.route("/")
def lukuvinkit():
    vinkit = [
        kirjavinkki("testiotsikko", "testikirjailija", "1970", "testaaja"),
        kirjavinkki("testiotsikko2")
    ]
    return render_template("lukuvinkit.html", vinkit=vinkit)
