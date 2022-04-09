from os import getenv
from flask import Flask
from config import DATABASE_URL
from database import database
from views import lukuvinkit, uusi_vinkki, kirjautuminen


def create_app(testing: bool = False):
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['TESTING'] = testing

    database.init_app(app)

    app.register_blueprint(lukuvinkit.lukuvinkit_bp)
    app.register_blueprint(uusi_vinkki.uusi_lukuvinkki_bp)
    app.register_blueprint(kirjautuminen.kirjautuminen_bp)
    return app
