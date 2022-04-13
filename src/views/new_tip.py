from flask import render_template, Blueprint, redirect, request, session, flash
from services.book_tip_service import book_tip_service

new_tip_bp = Blueprint("new_tip", __name__)


@new_tip_bp.route("/new_tip", methods=["GET", "POST"])
def new_tip():
    if "username" not in session:
        flash(
            "Sinun pitää olla kirjautuneena jotta voit lisätä uuden vinkin", "error")
        return redirect("/login")

    title = ""
    author = ""
    year = ""
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]
        omistaja = session["username"]

        error = book_tip_service.add_book_tip(title, author, year, omistaja)

        if not error:
            return redirect("/")
        flash(error, "error")

    return render_template(
        "new_tip.html",
        title=title,
        author=author,
        year=year
    )
