import logging
from os import getenv
from flask import Flask
from flask import session  # pylint: disable=unused-import
from config import DATABASE_URL, ENV
from database import database
from views import login, new_tip, register, tips, tests


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    database.init_app(app)

    app.register_blueprint(tips.tips_bp)
    app.register_blueprint(new_tip.new_tip_bp)
    app.register_blueprint(login.login_bp)
    app.register_blueprint(register.register_bp)
    if ENV == "testing":
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        app.register_blueprint(tests.tests_bp)
    return app
