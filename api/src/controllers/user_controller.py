from src.controllers.utils import *
from pymongo import ReturnDocument

class UserController():
    @staticmethod
    def getAllUsers():
        users = list(mongo.db.user.find())
        return JSONEncoder().encode(users)

    @staticmethod
    def getAllOfRole(userRole):
        users = list(mongo.db.user.find({"role": userRole}))
        return JSONEncoder().encode(users)
    
    @staticmethod
    def getAllLearnersInClass(courseCode, classCode):
        users = list(mongo.db.user.find({
            "$and": [{"role": "learner"}, {"enrolledCourses." + courseCode: classCode}]}))
        return JSONEncoder().encode(users)
    
    @staticmethod
    def getAllPendingLearnersInClass(courseCode, classCode):
        users = list(mongo.db.user.find({
            "$and": [{"role": "learner"}, {"pendingCourses." + courseCode: classCode}]}))
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
