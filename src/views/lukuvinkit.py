from flask import render_template, Blueprint, redirect, request
from entities.kirjavinkki import Kirjavinkki

lukuvinkit_bp = Blueprint("lukuvinkit", __name__)

vinkit = [
    Kirjavinkki("testiotsikko", "testikirjailija", "1970", "testaaja"),
    Kirjavinkki("testiotsikko2")
]


@lukuvinkit_bp.route("/")
def lukuvinkit():
    return render_template("lukuvinkit.html", vinkit=vinkit)


@lukuvinkit_bp.route("/uusi_vinkki")
def uusi_vinkki():
    return render_template("uusi_vinkki.html")


@lukuvinkit_bp.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    try:
        otsikko = str(request.form["otsikko"])
        kirjailija = str(request.form["kirjailija"])
        kirjoitusvuosi = int(request.form["kirjoitusvuosi"])
        omistaja = str(request.form["omistaja"])

        vinkit.append(
            Kirjavinkki(otsikko, kirjailija, kirjoitusvuosi, omistaja)
        )
        return redirect("/")
    except:
        return render_template("virhe.html")
