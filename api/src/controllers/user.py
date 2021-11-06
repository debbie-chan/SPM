class Learner:
    def __init__(self, learnerDoc):
        self.__learnerDoc = learnerDoc

    def ifPreReqMet(self, preRequisites):
        status = True
        for c in preRequisites:
            if c not in self.__learnerDoc["completedCourses"]:
                status = False
        return status

    def ifNotCompleted(self, courseCode):
        return courseCode not in self.__learnerDoc["completedCourses"]

    def ifNotEnrolled(self, courseCode):
        return courseCode not in self.__learnerDoc["enrolledCourses"]
