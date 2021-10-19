from main import *

# class User():
#     userID = db.Column(db.String, primary_key=True)
#     username = db.Column(db.String(50))
#     password = db.Column(db.String(1000))
#     designation = db.Column(db.String())
#     department = db.Column(db.String)


# class Admin(User):
#     def assignLearnerToCourse(self, learner, course):
#         pass

# class Trainer(User):
#     def createQuiz(self):
#         pass

# class Learner(User):
#     __tablename__ = "learner"

#     enrolledCourses = db.
#     attemptedCourses = db.Column(db.String)
#     completedCourses = db.Column(db.String)

#     def addEnrolledCourse(CourseID):
#         pass


@app.route('/')
def getAllUsers():
    users = list(userdb.user.find())
    return jsonify({"users": users})

@app.route('/admin')
def getAllAdmins():
    users = list(userdb.user.find({"roles":"admin"}))
    return jsonify({"users": users})

@app.route('/trainer')
def getAllTrainers():
    users = list(userdb.user.find({"roles":"trainer"}))
    return jsonify({"users": users})

@app.route('/learner')
def getAllLearners():
    users = list(userdb.user.find({"roles":"learner"}))
    return jsonify({"users": users})

@app.route('/user/<string:userId>', methods=['GET'])
def getOneUser(userId):
    oneUser = userdb.user.find_one({"_id": userId})
    return oneUser

@app.route("/learner/<string:userId>/<string:courseId>/selfEnroll")
def selfEnroll(userId, courseId):
    result = userdb.learner.find_one_and_update(
                {"_id": userId}, 
                {"$push": {"enrolledCourses":courseId}})
    return result

# @app.route("/addUser")
# def addUser():
#     userDocument = {"_id":"5",
#                     "username":"admin",
#                     "password":"password",
#                     "roles":["admin"]}
#     userdb.user.insert_one(userDocument)
#     return jsonify(message="success")

    