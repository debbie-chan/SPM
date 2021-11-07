from src.controllers.utils import JSONEncoder
from src.database import mongo


class Quiz:
    def __init__(self, QuizDoc):
        self.__QuizDoc = QuizDoc
        
    @staticmethod
    def getQuiz(lessonCode):
        lessonDoc = mongo.db.lesson.find_one_or_404({"lessonCode": lessonCode})
        quiz = lessonDoc["quiz"]
        return JSONEncoder().encode(quiz), 200

    @staticmethod
    def getFinalGrade(username, courseCode):
        userDoc = mongo.db.user.find_one_or_404({"username": username})
        finalGrade = userDoc["quizResults"][courseCode]
        return JSONEncoder().encode(finalGrade), 200

    @staticmethod
    def updateCompletedCourses(username):
        pass
