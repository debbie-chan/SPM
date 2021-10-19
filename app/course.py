from main import *
import datetime

# class Course():
#     __tablename__ = "course"

#     CourseID = db.Column(db.String, primary_key=True)
#     CourseName = db.Column(db.String(50))
#     CourseDescription = db.Column(db.String(1000))
#     PreRequisites = db.Column(db.List())

#     def getEnrolledLearners(self):
#         pass

# class EnrolledLearners(Course):
#     __tablename__ = 'enrolledLearners'

    

# class Class(Course):
#     __tablename__ = "class"

#     ClassId = db.Column(db.String)
#     ClassName = db.Column(db.String)
#     StartDate = db.Column(db.Date)
#     EndDate = db.Column(db.Date)
#     StartTime = db.Column(db.Time)
#     EndTime = db.Column(db.Time)
#     ClassSize = db.Column(db.Integer)
#     TrainerID = db.Column(db.String)
#     MaxEnrollment = db.Column(db.Integer)
#     EnrollmentStartDate = db.Column(db.Date)
#     EnrollmentEndDate = db.Column(db.Date)


# class Chapter(Class):
#     __tablename__ = "chapter"

#     SectionID = db.Column(db.Integer)
#     SectionName = db.Column(db.String)
    


@app.route('/courses', methods=['GET'])
def getAllCourses():
    courses = list(coursedb.course.find())
    return jsonify({"courses": courses})

@app.route('/courses/<string:courseId>', methods=['GET'])
def getOneCourse(courseId):
    oneCourse = coursedb.course.find_one({"_id": courseId})
    return oneCourse

@app.route("/addCourse")
def addCourse():
    courseDocument = {"_id":"IS113",
                    "courseName":"Web Application Development I",
                    "courseDescription":"WAD",
                    "preRequisites":["IS111"]}
    coursedb.course.insert_one(courseDocument)
    return jsonify(message="success")
