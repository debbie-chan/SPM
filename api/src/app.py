from flask import Flask
from flask_cors import CORS
import certifi

from .controllers.user_controller import (
    UserController,
    AdminController,
    LearnerController,
)
from .controllers.course_controller import (
    CourseController,
    ClassController,
    LessonController,
)
from .controllers.quiz import Quiz
from .controllers.quiz_controller import QuizController
from .controllers.question_controller import QuestionController
from .database import mongo


def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.static_folder = "../../dist/static"
    app.template_folder = "../../dist"
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config["MONGO_URI"] = db_uri
    mongo.init_app(app, tlsCAFile=certifi.where())

    # user routes
    app.add_url_rule(
        "/api", methods=["GET"], view_func=UserController.getAllUsers
    )
    app.add_url_rule(
        "/api/<string:userRole>",
        methods=["GET"],
        view_func=UserController.getAllOfRole,
    )
    app.add_url_rule(
        "/api/<string:userRole>/<string:username>",
        methods=["GET"],
        view_func=UserController.getOneUser,
    )
    app.add_url_rule(
        "/api/getEnrolledLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getEnrolledLearners,
    )
    app.add_url_rule(
        "/api/getPendingLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getPendingLearners,
    )
    app.add_url_rule(
        "/api/getUnenrolledLearners/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=UserController.getUnenrolledLearners,
    )
    app.add_url_rule(
        "/api/createUser",
        methods=["POST"],
        view_func=UserController.createUser,
    )

    # admin routes
    app.add_url_rule(
        "/api/assignLearnerToClass/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.assignLearnerToClass,
    )
    app.add_url_rule(
        "/api/verifyLearner/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.verifyLearner,
    )
    app.add_url_rule(
        "/api/assignTrainerToClass/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=AdminController.assignTrainerToClass,
    )

    # learner routes
    app.add_url_rule(
        "/api/addPendingCourse/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=LearnerController.addPendingCourse,
    )
    app.add_url_rule(
        "/api/deletePendingCourse/<string:username>/<string:courseCode>"
        "/<string:classCode>",
        methods=["GET"],
        view_func=LearnerController.deletePendingCourse,
    )

    # question/quiz routes
    app.add_url_rule(
        "/api/addQuestions",
        methods=["POST"],
        view_func=QuestionController.addQuestions,
    )
    app.add_url_rule(
        "/api/getQuiz/<string:lessonCode>",
        methods=["GET"],
        view_func=Quiz.getQuiz,
    )
    app.add_url_rule(
        "/api/gradeQuiz", methods=["POST"], view_func=QuizController.gradeQuiz
    )
    app.add_url_rule(
        "/api/getFinalGrade/<string:username>/<string:courseCode>",
        methods=["GET"],
        view_func=Quiz.getFinalGrade,
    )

    # course routes
    app.add_url_rule(
        "/api/course",
        methods=["GET"],
        view_func=CourseController.getAllCourses,
    )
    app.add_url_rule(
        "/api/course/<string:courseCode>",
        methods=["GET"],
        view_func=CourseController.getOneCourse,
    )
    app.add_url_rule(
        "/api/course/<string:courseCode>/classes",
        methods=["GET"],
        view_func=CourseController.getAllClassesInCourse,
    )
    app.add_url_rule(
        "/api/course/createCourse",
        methods=["POST"],
        view_func=CourseController.createCourse,
    )
    app.add_url_rule(
        "/api/course/displayAllCourses",
        methods=["GET"],
        view_func=CourseController.displayAllCourses,
    )

    # class routes
    app.add_url_rule(
        "/api/class", methods=["GET"], view_func=ClassController.getAllClasses
    )
    app.add_url_rule(
        "/api/class/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=ClassController.getOneClass,
    )
    app.add_url_rule(
        "/api/class/createClass",
        methods=["POST"],
        view_func=ClassController.createClass,
    )

    # lesson routes
    app.add_url_rule(
        "/api/lessons/<string:courseCode>/<string:classCode>",
        methods=["GET"],
        view_func=LessonController.getAllLessonsInClass,
    )
    app.add_url_rule(
        "/api/lesson/createLesson",
        methods=["POST"],
        view_func=LessonController.createLesson,
    )

    return app
