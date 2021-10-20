from main import *

class Quiz():
    def __init__(self, id, quizName):
        self.__id = id
        self.__quizName = quizName
        self.__questions = []
    
    def addQuestion(self, question):
        self.__questions.append(question)

class Question():
    def __init__(self, prompt, options, answer):
        self.__prompt = prompt
        self.__options = options
        self.__answer = answer