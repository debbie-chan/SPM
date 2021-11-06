from flask import request
from pymongo import ReturnDocument
from src.controllers.utils import JSONEncoder
from src.database import mongo


class QuizController:
    @staticmethod
    def gradeQuiz():
        """
        attempt = {"username": "edsheeran",
                    "lessonCode": "X1010G1L2",
                    "courseCode": "X1010",
                    "classCode": "G1",
                    "answer1" : "3",
                    "answer2" : "1"
                    }

        quiz = {"q1" : "Question1",
                "options1" : ['Option1', 'Option2', 'Option3', 'Option4'],
                "answer1" : "Option3",
                "q2" : "Question2",
                "options2" :['0', '1'],
                "answer2" : "1"
                }
        """
        attempt = request.get_json()
        lessonCode = attempt["lessonCode"]
        courseCode = attempt["courseCode"]
        classCode = attempt["classCode"]
        username = attempt["username"]
        attempt.pop("username")
        attempt.pop("lessonCode")
        attempt.pop("courseCode")
        attempt.pop("classCode")

        lessonDoc = mongo.db.lesson.find_one_or_404({"lessonCode": lessonCode})
        quiz = lessonDoc["quiz"]

        marks = 0
        total_marks = len(attempt)

        for key in attempt:
            if key in quiz.keys():
                if attempt[key] == quiz[key]:
                    marks += 1

        marks = marks / total_marks

        if marks >= 0.85:
            grade = "Pass"
        else:
            grade = "Fail"

        classDocument = mongo.db["class"].find_one_or_404(
            {"$and": [{"courseCode": courseCode}, {"classCode": classCode}]}
        )
        lessonCode = int(lessonCode[-1])
        numLessons = int(classDocument["numLessons"])
        if lessonCode == numLessons:
            results = {courseCode: grade}
            data = mongo.db.user.find_one_and_update(
                {"username": username},
                {"$set": {"quizResults": results}},
                return_document=ReturnDocument.AFTER,
            )
            return JSONEncoder().encode(data), 200
        else:
            return grade
