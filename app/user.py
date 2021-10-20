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

    def addEnrolledCourse(courseId):
        pass

# get users
@app.route('/')
def getAllUsers():
    users = list(userdb.user.find())
    return jsonify({"users": users}), 200

@app.route('/admin')
def getAllAdmins():
    users = list(userdb.user.find({"roles.role":"admin"}))
    return jsonify({"admins": users}), 200

@app.route('/trainer')
def getAllTrainers():
    users = list(userdb.user.find({"roles.role":"trainer"}))
    return jsonify({"trainers": users}), 200

@app.route('/learner')
def getAllLearners():
    users = list(userdb.user.find({"roles.role":"learner"}))
    pprint(users)
    return jsonify({"learners": users}), 200

@app.route('/user/<string:userId>', methods=['GET'])
def getOneUser(userId):
    oneUser = userdb.user.find_one_or_404({"_id": userId})
    return oneUser


# methods
@app.route("/learner/<string:userId>/selfEnroll/<string:courseId>")
def selfEnroll(userId, courseId):
    try:
        Learner.addEnrolledCourse(courseId)
    except Exception:
        return jsonify({"message": "No."}), 500
    
    out = userdb.user.find_one_and_update(
                {"$and": [{"_id": userId}, {"roles.role":"learner"}]}, 
                {"$push": {"roles.enrolledCourses": courseId}})
    return out


# add new users
@app.route("/addAdmin")
def addAdmin():
    userDocument = {"_id":"1",
                    "username":"adminUser",
                    "password":"password",
                    "roles":[{"role":"admin"}]}
    out = userdb.user.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200

@app.route("/addTrainer")
def addTrainer():
    userDocument = {"_id":"2",
                    "username":"trainerUser",
                    "password":"password",
                    "roles":[{"role":"trainer",
                                "trainingCourses":["IS111","CS2030"],
                                "trainedCourses":["IS110"]}]}
    out = userdb.user.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200

@app.route("/addLearner")
def addLearner():
    userDocument = {"_id":"3",
                    "username":"learnerUser",
                    "password":"password",
                    "roles":[{"role":"learner",
                                "enrolledCourses":["IS111","CS2030"],
                                "attemptedCourses":["IS110"],
                                "completedCourses":["CS1010"]}]}
    out = userdb.user.insert_one(userDocument)
    return jsonify({"id":out.inserted_id}), 200
