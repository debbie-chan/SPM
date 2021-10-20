from main import *

class User():
    def __init__(self, id, username, roles):
        self.__id = id
        self.__username = username
        self.__roles = roles

class Admin(User):
    def __init__(self, id, username, roles):
        User.__init__(self, id, username, roles)

    def assignLearnerToCourse(self, Learner, Course):
        pass

class Trainer(User):
    def __init__(self, id, username, roles):
        User.__init__(self, id, username, roles)
        
    def createQuiz(self):
        pass

class Learner(User):
    def __init__(self, id, username, roles):
        User.__init__(self, id, username, roles)
        self.__attemptedCourses = attemptedCourses

    def selfEnroll(courseId):
        ifAttempted = courseId in self.__attemptedCourses
        return ifAttempted

# get users
@app.route('/<string:userRole>')
def getAllUsers(userRole):
    users = list(userdb[userRole].find())
    pprint(users)
    return jsonify({userRole + "s": users}), 200

@app.route('/<string:userRole>/<string:userId>', methods=['GET'])
def getOneUser(userRole, userId):
    oneUser = userdb[userRole].find_one_or_404({"_id": userId})
    return oneUser


# methods
@app.route("/learner/<string:userId>/selfEnroll/<string:courseId>")
def addEnrolledCourse(userId, courseId):
    try:
        Learner.selfEnroll(courseId)
    except Exception:
        return jsonify({"message": "No."}), 500
    
    out = userdb.learner.find_one_and_update({
            {"_id": userId}, 
            {"$push": {"enrolledCourses": courseId}}})
    return out


# add new users
@app.route("/addAdmin")
def addAdmin():
    userDocument = {"_id":"1",
                    "username":"adminUser",
                    "password":"password"}
    out = userdb.admin.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200

@app.route("/addTrainer")
def addTrainer():
    userDocument = {"_id":"1",
                    "username":"trainerUser",
                    "password":"password",
                    "trainingCourses":["IS111","CS2030"],
                    "trainedCourses":["IS110"]}
    out = userdb.trainer.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200

@app.route("/addLearner")
def addLearner():
    userDocument = {"_id": "1",
                    "username": "learnerUser",
                    "password": "password",
                    "enrolledCourses": ["IS111","CS2030"],
                    "attemptedCourses": ["IS110"],
                    "completedCourses": ["CS1010"],
                    "quizResults": {
                        "CS2030": {"1": 10, "2": 10},
                        "CS1010": {"1": 10, "2": 10}}}
    out = userdb.learner.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200
