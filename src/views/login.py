from flask import Blueprint, render_template, redirect, flash, request, session
from services.user_service import user_service

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    username = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = user_service.log_in(username, password)
        if not error:
            session["username"] = username
            return redirect("/")
        flash(error, "error")

    return render_template("login.html", username=username)


@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")
