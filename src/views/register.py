from flask import Blueprint, render_template, redirect, flash, request, session
from services.user_service import user_service

register_bp = Blueprint("register", __name__)


@register_bp.route("/register", methods=["GET", "POST"])
def register():
    username = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        error = user_service.register(username, password)
        if not error:
            session["username"] = username
            return redirect("/")
        flash(error, "error")

    return render_template("register.html", username=username)
