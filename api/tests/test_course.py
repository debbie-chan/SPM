import unittest
from datetime import datetime
from src.controllers.course import Course, Class


# Led By: Deborah Chan
class TestCourse(unittest.TestCase):
    def setUp(self):
        Co1 = {"preRequisites": ["X100"]}
        Co2 = {"preRequisites": ["X200"]}

        self.__Course1 = Course(Co1)
        self.__Course2 = Course(Co2)

    def tearDown(self):
        self.__Course1 = None
        self.__Course2 = None

    def test_getPreRequisites(self):
        self.assertEqual(self.__Course1.getPreRequisites(), ["X100"])
        self.assertEqual(self.__Course2.getPreRequisites(), ["X200"])


# Led By: Deborah Chan
class TestClass(unittest.TestCase):
    def setUp(self):
        Cl1 = {
            "startDate": datetime(2021, 11, 1),
            "endDate": datetime(2021, 12, 1),
            "startTime": datetime(2021, 11, 1),
            "endTime": datetime(2021, 12, 1),
            "maxEnrollment": 45,
            "currentEnrollment": 30,
            "enrollmentStartDate": datetime(2021, 11, 1),
            "enrollmentEndDate": datetime(2021, 12, 1),
        }

        Cl2 = {
            "startDate": datetime(2021, 11, 1),
            "endDate": datetime(2021, 12, 1),
            "startTime": datetime(2021, 11, 1),
            "endTime": datetime(2021, 12, 1),
            "maxEnrollment": 45,
            "currentEnrollment": 45,
            "enrollmentStartDate": datetime(2021, 10, 1),
            "enrollmentEndDate": datetime(2021, 11, 1),
        }

        self.__Class1 = Class(Cl1)
        self.__Class2 = Class(Cl2)

    def tearDown(self):
        self.__Class1 = None
        self.__Class2 = None

    def test_ifNotFull(self):
        self.assertEqual(self.__Class1.ifNotFull(), True)
        self.assertEqual(self.__Class2.ifNotFull(), False)

    def test_ifEnrollmentOpen(self):
        self.assertEqual(self.__Class1.ifEnrollmentOpen(), True)
        self.assertEqual(self.__Class2.ifEnrollmentOpen(), False)
