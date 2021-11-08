class Learner:
    def __init__(self, learnerDoc):
        self.__learnerDoc = learnerDoc

    def ifPreReqMet(self, preRequisites):
        status = True
        for c in preRequisites:
            if c not in self.__learnerDoc["completedCourses"]:
                status = False
        return status

    def ifCompleted(self, courseCode):
        return courseCode in self.__learnerDoc["completedCourses"]

    def ifEnrolled(self, courseCode):
        return courseCode in self.__learnerDoc["enrolledCourses"]
