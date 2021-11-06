from flask import Flask
from flask_cors import CORS
import certifi

from src.controllers.user_controller import (
    UserController,
    AdminController,
    LearnerController,
)
from src.database import mongo


def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    CORS(app)
    app.config["MONGO_URI"] = db_uri
    mongo.init_app(app, tlsCAFile=certifi.where())

    # user routes
    app.add_url_rule(
        "/", methods=["GET"], view_func=UserController.getAllUsers
    )
    app.add_url_rule(
        "/<string:userRole>",
        methods=["GET"],
        view_func=UserController.getAllOfRole,
    )
    app.add_url_rule(
        "/<string:userRole>/<string:username>",
        methods=["GET"],
        view_func=UserController.getOneUser,
    )
    app.add_url_rule(
        "/getEnrolledLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getEnrolledLearners,
    )
    app.add_url_rule(
        "/getPendingLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getPendingLearners,
    )
    app.add_url_rule(
        "/getUnenrolledLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getUnenrolledLearners,
    )
    app.add_url_rule(
        "/createUser", methods=["POST"], view_func=UserController.createUser
    )

    # admin routes
    app.add_url_rule(
        "/assignLearnerToClass/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.assignLearnerToClass,
    )
    app.add_url_rule(
        "/assignTrainerToClass/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.assignTrainerToClass,
    )

    # learner routes
    app.add_url_rule(
        "/addPendingCourse/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=LearnerController.addPendingCourse,
    )
    app.add_url_rule(
        "/deletePendingCourse/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=LearnerController.deletePendingCourse,
    )

    return app
