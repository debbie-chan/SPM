from datetime import datetime


class Course:
    def __init__(self, courseDoc):
        self.__courseDoc = courseDoc

    def getPreRequisites(self):
        try:
            return self.__courseDoc["preRequisites"]
        except Exception:
            return []


class Class:
    def __init__(self, classDoc):
        self.__classDoc = classDoc

    def ifNotFull(self):
        return (
            self.__classDoc["currentEnrollment"]
            < self.__classDoc["maxEnrollment"]
        )

    def ifEnrollmentOpen(self):
        return (
            self.__classDoc["enrollmentStartDate"]
            <= datetime.now()
            <= self.__classDoc["enrollmentEndDate"]
        )
