import unittest
from ..src.controllers.user import Learner


# Led By: Deborah Chan
class TestLearner(unittest.TestCase):
    def test_ifPreReqMet(self):
        Learner1 = Learner({"completedCourses": {"X100": "G1"}})
        self.assertEqual(Learner1.ifPreReqMet(["X100"]), True)
        self.assertEqual(Learner1.ifPreReqMet(["X100", "X200"]), False)

    def test_ifCompleted(self):
        Learner1 = Learner({"completedCourses": {"X100": "G1"}})
        self.assertEqual(Learner1.ifCompleted("X100"), True)
        self.assertEqual(Learner1.ifCompleted("X200"), False)

    def test_ifEnrolled(self):
        Learner1 = Learner({"enrolledCourses": {"X200": "G1"}})
        self.assertEqual(Learner1.ifEnrolled("X200"), True)
        self.assertEqual(Learner1.ifEnrolled("X300"), False)
