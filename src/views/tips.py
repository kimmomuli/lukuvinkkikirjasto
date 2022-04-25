from flask import Blueprint, render_template, request, session
from repositories.tip_repository import tip_repository

tips_bp = Blueprint("tips", __name__)


@tips_bp.route("/", methods=["GET", "POST"])
def tips_route():
    tips = tip_repository.get_all_tips()
    if request.method == "POST":
        for tip in tips:
            if (request.form.get(f"delete_{tip.type}_{tip.title}")
                    and tip.adder_username == session["username"]):
                tip_repository.delete_tip(tip)
        tips = tip_repository.get_all_tips()
    return render_template("tips.html", tips=tips)
