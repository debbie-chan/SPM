from flask import request
from pymongo import ReturnDocument
from src.controllers.utils import JSONEncoder
from src.database import mongo


class QuestionController:
    @staticmethod
    def addQuestions():
        """
        From FE:
        data = {
            "lessonCode": "X1010G1L1",
            "q1" : "Question1",
            "options1" : ['1', '2', '3', '4'],
            "answer1" : "Option2",
            "q2" : "Question2",
            "options2" :['Option1', 'Option2', 'Option3', 'Option4'],
            "answer2" : "Option4"
        }
        """
        data = request.get_json(force=True)
        lessonCode = data["lessonCode"]
        data.pop("lessonCode")
        quiz = mongo.db.lesson.find_one_and_update(
            {"lessonCode": lessonCode},
            {"$set": {"quiz": data}},
            return_document=ReturnDocument.AFTER,
        )
        return JSONEncoder().encode(quiz)
