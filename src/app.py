from os import getenv
from flask import Flask
from config import DATABASE_URL


def create_app(testing: bool = False):
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['TESTING'] = testing

    from database import database
    database.init_app(app)

    from views import lukuvinkit
    app.register_blueprint(lukuvinkit.lukuvinkit_bp)
    return app
