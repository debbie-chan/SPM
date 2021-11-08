import unittest
from unittest.mock import patch
from mongomock import MongoClient
from ..src.app import create_app
from ..src import database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Joslyn Ho
class TestCourseController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getAllCourses(self):
        response = self.app.get("/api/course")
        self.assertEqual(response.status_code, 200)

    def test_getOneCourse(self):
        response_valid = self.app.get("/api/course/X1010")
        response_invalid = self.app.get("/api/course/ABC")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getAllClassesInCourse(self):
        response = self.app.get("/api/course/X1010/classes")
        self.assertEqual(response.status_code, 200)

    def test_displayAllCourses(self):
        response = self.app.get("/api/course/displayAllCourses")
        self.assertEqual(response.status_code, 200)


# Led By: Joslyn Ho
class TestClassController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getAllClasses(self):
        response = self.app.get("/api/class")
        self.assertEqual(response.status_code, 200)

    def test_getOneClass(self):
        response_valid = self.app.get("/api/class/X1010/G1")
        response_invalid = self.app.get("/api/class/ABC")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)


# Led By: Joslyn Ho
class TestLessonController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getAllLessonsInClass(self):
        response = self.app.get("/api/lessons/X1010/G1")
        self.assertEqual(response.status_code, 200)
