from flask import Blueprint, redirect, flash, request, session
from repositories.tip_repository import tip_repository

like_bp = Blueprint("like", __name__)


@like_bp.route("/like", methods=["POST"])
def like():
    tip_id = request.form["tip_id"]
    if tip_repository.add_like(tip_id, session["username"]):
        return redirect("/")
    flash("Tykkääminen epäonnistui", "error")
    return redirect("/")


@like_bp.route("/dislike", methods=["POST"])
def dislike():
    tip_id = request.form["tip_id"]
    if tip_repository.remove_like(tip_id, session["username"]):
        return redirect("/")
    flash("Tykkäämisen poisto epäonnistui", "error")
    return redirect("/")
