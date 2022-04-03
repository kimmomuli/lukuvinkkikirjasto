from os import getenv
from flask import Flask
from config import DATABASE_URL
from database import database
from views import lukuvinkit



def create_app(testing: bool = False):
    app = Flask(__name__)
    app.secret_key = getenv("SECRET_KEY")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config['TESTING'] = testing

    database.init_app(app)

    app.register_blueprint(lukuvinkit.lukuvinkit_bp)
    return app
