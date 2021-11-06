from flask import Flask
from flask_cors import CORS
import certifi

from src.controllers.user_controller import (
    UserController,
    AdminController,
    LearnerController,
)
from src.controllers.course_controller import (
    CourseController,
    ClassController,
    LessonController,
)
from src.controllers.quiz import Quiz
from src.controllers.quiz_controller import QuizController
from src.controllers.question_controller import QuestionController
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
        "/verifyLearner/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.verifyLearner,
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

    # question/quiz routes
    app.add_url_rule(
        "/addQuestions",
        methods=["POST"],
        view_func=QuestionController.addQuestions,
    )
    app.add_url_rule(
        "/getQuiz/<string:lessonCode>", methods=["GET"], view_func=Quiz.getQuiz
    )
    app.add_url_rule(
        "/gradeQuiz", methods=["POST"], view_func=QuizController.gradeQuiz
    )
    app.add_url_rule(
        "/getFinalGrade/<string:username>/<string:courseCode>",
        methods=["GET"],
        view_func=Quiz.getFinalGrade,
    )

    
    # course routes
    app.add_url_rule(
        "/course", methods=["GET"], view_func=CourseController.getAllCourses
    )
    app.add_url_rule(
        "/course/<string:courseCode>",
        methods=["GET"],
        view_func=CourseController.getOneCourse,
    )
    app.add_url_rule(
        "/course/<string:courseCode>/classes",
        methods=["GET"],
        view_func=CourseController.getAllClassesInCourse,
    )
    app.add_url_rule(
        "/course/createCourse",
        methods=["POST"],
        view_func=CourseController.createCourse,
    )

    # class routes
    app.add_url_rule(
        "/class", methods=["GET"], view_func=ClassController.getAllClasses
    )
    app.add_url_rule(
        "/class/<string:classCode>",
        methods=["GET"],
        view_func=ClassController.getOneClass,
    )
    app.add_url_rule(
        "/class/createClass",
        methods=["POST"],
        view_func=ClassController.createClass,
    )

    # lesson routes
    app.add_url_rule(
        "/lessons/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=LessonController.getAllLessonsInClass,
    )
    app.add_url_rule(
        "/lesson/createLesson",
        methods=["POST"],
        view_func=LessonController.createLesson,
    )

    return app
