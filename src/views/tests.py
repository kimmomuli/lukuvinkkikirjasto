from flask import Blueprint, request
from repositories.user_repository import user_repository
from repositories.tip_repository import tip_repository
from services.book_tip_service import book_tip_service

tests_bp = Blueprint("test", __name__)


@tests_bp.route("/tests/reset", methods=["POST"])
def reset():
    user_repository.delete_all()
    tip_repository.delete_all()
    return "ok"


@tests_bp.route("/tests/add_book_tip", methods=["POST"])
def add_book_tip():
    title = request.json["title"]
    author = request.json["author"]
    year = request.json["year"]
    adder_username = request.json["adder_username"]
    book_tip_service.add_book_tip(title, author, year, adder_username)
    return "ok"
