import unittest
from datetime import datetime
from ..src.controllers.course import Course, Class


# Led By: Deborah Chan
class TestCourse(unittest.TestCase):
    def test_getPreRequisites(self):
        Course1 = Course({})
        Course2 = Course({"preRequisites": []})
        Course3 = Course({"preRequisites": ["X200", "X300"]})
        self.assertEqual(Course1.getPreRequisites(), [])
        self.assertEqual(Course2.getPreRequisites(), [])
        self.assertEqual(Course3.getPreRequisites(), ["X200", "X300"])


# Led By: Deborah Chan
class TestClass(unittest.TestCase):
    def test_ifFull(self):
        Class1 = Class(
            {
                "maxEnrollment": 45,
                "currentEnrollment": 45,
            }
        )
        Class2 = Class(
            {
                "maxEnrollment": 45,
                "currentEnrollment": 30,
            }
        )
        self.assertEqual(Class1.ifFull(), True)
        self.assertEqual(Class2.ifFull(), False)

    def test_ifEnrollmentOpen(self):
        Class1 = Class(
            {
                "enrollmentStartDate": datetime(2021, 11, 1),
                "enrollmentEndDate": datetime(2021, 12, 1),
            }
        )
        Class2 = Class(
            {
                "enrollmentStartDate": datetime(2021, 10, 1),
                "enrollmentEndDate": datetime(2021, 11, 1),
            }
        )
        self.assertEqual(Class1.ifEnrollmentOpen(), True)
        self.assertEqual(Class2.ifEnrollmentOpen(), False)
