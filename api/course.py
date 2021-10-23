from main import *

class Course():
    def slotsAvailable(self):
        return currentEnrollment < maxEnrollment

# class Class(Course):

# class Lesson(Class):


@app.route('/courses', methods=['GET'])
def getAllCourses():
    courses = list(coursedb.course.find())
    return jsonify({"courses": courses})

@app.route('/courses/<string:courseId>', methods=['GET'])
def getOneCourse(courseId):
    oneCourse = coursedb.course.find_one({"_id": courseId})
    return oneCourse

# file upload
# @app.route("/uploads/<path:filename>", methods=["POST"])
# def saveUpload(filename):
#     coursedb.course.save_file(filename, request.files["file"])
#     return redirect(url_for("get_upload", filename=filename))

# @app.route("/uploads/<path:filename>")
# def getUpload(filename):
#     return coursedb.course.send_file(filename)

# add course / class / lesson
@app.route("/addCourse")
def addCourse():
    courseDocument = {"_id":"IS113",
                    "courseName":"Web Application Development I",
                    "courseDescription":"WAD",
                    "preRequisites":["IS111"]}
    coursedb.course.insert_one(courseDocument)
    return jsonify(message="success")

@app.route("/addClass")
def addClass():
    classDocument = {"_id": "G1",
                    "className": "G1",
                    "trainerID": 1,
                    "startDate": datetime(2021, 1, 1),
                    "endDate": datetime(2021, 1, 1),
                    "startTime": datetime(2021, 1, 1),
                    "endTime": datetime(2021, 1, 1),
                    "currentEnrollment": 30,
                    "maxEnrollment": 45,
                    "enrollmentStartDate": datetime(2021, 1, 1),
                    "enrollmentEndDate": datetime(2021, 1, 1),
                    "classQuiz": {
                        "quizName": "Quiz 1",
                        "timeLimit": 100,
                        "questions": {
                            1: {
                                "prompt": "Why did the chicken cross the road?",
                                "options": ["because", "yes", "no", "idk"],
                                "answer": "yes"
                                },
                            2: {
                                "prompt": "How did the chicken cross the road?",
                                "options": ["because", "yes", "no", "idk"],
                                "answer": "yes"
                            }}}}
    coursedb["class"].insert_one(classDocument)
    return jsonify(message="success")

@app.route("/addLesson")
def addLesson():
    lessonDocument = {"_id": "IS113",
                    "lessonName": "Week 1",
                    "lessonDescription": "WAD",
                    "lessonQuiz": {
                        1: {
                            "prompt": "Why did the chicken cross the road?",
                            "options": ["because", "yes", "no", "idk"],
                            "answer": "yes"
                            },
                        2: {
                            "prompt": "How did the chicken cross the road?",
                            "options": ["because", "yes", "no", "idk"],
                            "answer": "yes"
                        }}}
    coursedb.lesson.insert_one(lessonDocument)
    return jsonify(message="success")