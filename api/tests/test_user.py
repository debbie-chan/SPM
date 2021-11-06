import unittest
from src.controllers.user import Learner


# Led By: Deborah Chan
class TestLearner(unittest.TestCase):
    def setUp(self):
        L1 = {
            "employeeName": "Emma Jones",
            "username": "emmajones",
            "password": "password",
            "department": "Technology",
            "designation": "Junior Engineer",
            "role": "learner",
            "pendingCourses": {"pending1": "G1", "X2000": "G1"},
            "enrolledCourses": {"X1010": "G1", "T100": "G1"},
            "attemptedCourses": {"X200": "G1"},
            "completedCourses": {"X100": "G1"},
            "quizResults": {},
        }

        self.__Learner1 = Learner(L1)

    def tearDown(self):
        self.__Learner1 = None

    def test_ifPreReqMet(self):
        self.assertEqual(self.__Learner1.ifPreReqMet(["X100"]), True)
        self.assertEqual(self.__Learner1.ifPreReqMet(["X200"]), False)

    def test_ifNotCompleted(self):
        self.assertEqual(self.__Learner1.ifNotCompleted("X100"), False)
        self.assertEqual(self.__Learner1.ifNotCompleted("X200"), True)
