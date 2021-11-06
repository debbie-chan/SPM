from flask import request, jsonify
from pymongo import ReturnDocument
from src.controllers.utils import JSONEncoder
from src.database import mongo


class UserController:
    @staticmethod
    def getAllUsers():
        users = list(mongo.db.user.find())
        return JSONEncoder().encode(users)

    @staticmethod
    def getAllOfRole(userRole):
        users = list(mongo.db.user.find({"role": userRole}))
        return JSONEncoder().encode(users)

    @staticmethod
    def getEnrolledLearners(courseCode, classCode):
        users = list(
            mongo.db.user.find(
                {
                    "$and": [
                        {"role": "learner"},
                        {"enrolledCourses." + courseCode: classCode},
                    ]
                }
            )
        )
        return JSONEncoder().encode(users)

    @staticmethod
    def getPendingLearners(courseCode, classCode):
        users = list(
            mongo.db.user.find(
                {
                    "$and": [
                        {"role": "learner"},
                        {"pendingCourses." + courseCode: classCode},
                    ]
                }
            )
        )
        return JSONEncoder().encode(users)

    @staticmethod
    def getUnenrolledLearners(courseCode, classCode):
        users = list(
            mongo.db.user.find(
                {
                    "$and": [
                        {"role": "learner"},
                        {
                            "$nor": [
                                {"completedCourses." + courseCode: classCode},
                                {"enrolledCourses." + courseCode: classCode},
                                {"pendingCourses." + courseCode: classCode},
                            ]
                        },
                    ]
                }
            )
        )
        return JSONEncoder().encode(users)

    @staticmethod
    def getOneUser(userRole, username):
        oneUser = mongo.db.user.find_one_or_404({"username": username})
        return JSONEncoder().encode(oneUser)

    @staticmethod
    def createUser():
        data = request.get_json(force=True)
        mongo.db.user.insert_one(data)
        data["_id"] = str(data["_id"])
        return jsonify(data), 201


class AdminController:
    @staticmethod
    def assignTrainerToClass(username, courseCode, classCode):
        mongo.db["class"].find_one_and_update(
            {"$and": [{"courseCode": courseCode, "classCode": classCode}]},
            {"$set": {"trainerName": username}},
        )
        data = mongo.db.user.find_one_and_update(
            {"username": username},
            {"$set": {"trainingCourses." + courseCode: classCode}},
            return_document=ReturnDocument.AFTER,
        )
        return JSONEncoder().encode(data)

    @staticmethod
    def assignLearnerToClass(username, courseCode, classCode):
        data = mongo.db.user.find_one_and_update(
            {"username": username},
            {"$set": {"enrolledCourses." + courseCode: classCode}},
            return_document=ReturnDocument.AFTER,
        )
        return JSONEncoder().encode(data)


class LearnerController:
    @staticmethod
    def addPendingCourse(username, courseCode, classCode):
        data = mongo.db.user.find_one_and_update(
            {"username": username},
            {"$set": {"pendingCourses." + courseCode: classCode}},
            return_document=ReturnDocument.AFTER,
        )
        return JSONEncoder().encode(data)

    @staticmethod
    def deletePendingCourse(username, courseCode, classCode):
        data = mongo.db.user.find_one_and_update(
            {"username": username},
            {"$unset": {"pendingCourses." + courseCode: classCode}},
            return_document=ReturnDocument.AFTER,
        )
        return JSONEncoder().encode(data)
