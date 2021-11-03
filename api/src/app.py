from flask import Flask
from flask_cors import CORS
import certifi

from src.controllers import *
from src.database import mongo

def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config["MONGO_URI"] = db_uri
    mongo.init_app(app, tlsCAFile=certifi.where())

    # user routes
    app.add_url_rule("/", methods=["GET"], view_func=UserController.getAllUsers)
    app.add_url_rule("/<string:userRole>", methods=["GET"], view_func=UserController.getAllOfRole)
    app.add_url_rule("/getAllLearnersInClass/<string:courseCode>/<string:classCode>", methods=["GET"], view_func=UserController.getAllLearnersInClass)
    app.add_url_rule("/getAllPendingLearnersInClass/<string:courseCode>/<string:classCode>", methods=["GET"], view_func=UserController.getAllPendingLearnersInClass)
    app.add_url_rule("/<string:userRole>/<string:username>", methods=["GET"], view_func=UserController.getOneUser)
    app.add_url_rule("/createUser", methods=["POST"], view_func=UserController.createUser)

    return app