import logging
from os import getenv
from flask import Flask
from flask import session  # pylint: disable=unused-import
from config import DATABASE_URL, ENV
from database import database
from views import lukuvinkit, uusi_vinkki, kirjautuminen, rekisteroityminen, tests


def create_app():
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

    database.init_app(app)

    app.register_blueprint(lukuvinkit.lukuvinkit_bp)
    app.register_blueprint(uusi_vinkki.uusi_lukuvinkki_bp)
    app.register_blueprint(kirjautuminen.kirjautuminen_bp)
    app.register_blueprint(rekisteroityminen.rekisteroityminen_bp)
    if ENV == "testing":
        logging.getLogger('werkzeug').setLevel(logging.ERROR)
        app.register_blueprint(tests.tests_bp)
    return app
