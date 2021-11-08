from flask import request, jsonify
from .utils import JSONEncoder
from ..database import mongo


class CourseController:
    @staticmethod
    def getAllCourses():
        courses = list(mongo.db.course.find())
        return JSONEncoder().encode(courses), 200

    @staticmethod
    def getOneCourse(courseCode):
        oneCourse = mongo.db.course.find_one_or_404({"courseCode": courseCode})
        return JSONEncoder().encode(oneCourse), 200

    @staticmethod
    def getAllClassesInCourse(courseCode):
        classes = list(mongo.db["class"].find({"courseCode": courseCode}))
        return JSONEncoder().encode(classes), 200

    @staticmethod
    def createCourse():
        data = request.get_json(force=True)
        mongo.db.course.insert_one(data)
        data["_id"] = str(data["_id"])
        return jsonify(data), 201

    @staticmethod
    def displayAllCourses():
        courseDocs = list(mongo.db["course"].find())

        response = []
        for course in courseDocs:
            courseCode = course["courseCode"]
            preRequisites = course["preRequisites"]
            classDocs = list(
                mongo.db["class"].find({"courseCode": courseCode})
            )
            for classDoc in classDocs:
                resp_dict = {}
                courseName = course["courseName"]
                courseDescription = course["courseDescription"]
                resp_dict["courseCode"] = courseCode
                resp_dict["courseName"] = courseName
                resp_dict["courseDescription"] = courseDescription
                classCode = classDoc["classCode"]
                resp_dict["classCode"] = classCode
                resp_dict["preRequisites"] = preRequisites
                response.append(resp_dict)
        return JSONEncoder().encode(response), 200


class ClassController:
    @staticmethod
    def getAllClasses():
        classes = list(mongo.db["class"].find())
        return JSONEncoder().encode(classes), 200

    @staticmethod
    def getOneClass(classCode):
        oneClass = mongo.db["class"].find_one_or_404({"classCode": classCode})
        return JSONEncoder().encode(oneClass), 200

    @staticmethod
    def createClass():
        data = request.get_json(force=True)
        mongo.db["class"].insert_one(data)
        data["_id"] = str(data["_id"])
        return jsonify(data), 201


class LessonController:
    @staticmethod
    def getAllLessonsInClass(courseCode, classCode):
        lessons = list(
            mongo.db.lesson.find(
                {"$and": [{"courseCode": courseCode, "classCode": classCode}]}
            )
        )
        return JSONEncoder().encode(lessons), 200

    @staticmethod
    def createLesson():
        data = request.get_json(force=True)
        mongo.db.lesson.insert_one(data)
        data["_id"] = str(data["_id"])
        return jsonify(data), 201


# # file upload
# # @app.route("/uploads/<path:filename>", methods=["POST"])
# # def saveUpload(filename):
# #     coursedb.course.save_file(filename, request.files["file"])
# #     return redirect(url_for("get_upload", filename=filename))

# # @app.route("/uploads/<path:filename>")
# # def getUpload(filename):
# #     return coursedb.course.send_file(filename)
