from flask import Blueprint, redirect, flash, request, session
from repositories.tip_repository import tip_repository

like_bp = Blueprint("like", __name__)


@like_bp.route("/like", methods=["POST"])
def like():
    title = request.form["title"]
    author = request.form["author"]
    if tip_repository.add_like(title, author, session["username"]):
        return redirect("/")
    flash("Tykkääminen epäonnistui", "error")
    return redirect("/")


@like_bp.route("/dislike", methods=["POST"])
def dislike():
    title = request.form["title"]
    author = request.form["author"]
    if tip_repository.remove_like(title, author, session["username"]):
        return redirect("/")
    flash("Tykkäämisen poisto epäonnistui", "error")
    return redirect("/")
