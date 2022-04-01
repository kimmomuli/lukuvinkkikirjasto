from os import getenv
from flask import Flask

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

from views import lukuvinkit
app.register_blueprint(lukuvinkit.lukuvinkit_bp)