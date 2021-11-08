import unittest
from unittest.mock import patch
from mongomock import MongoClient
from ..src.app import create_app
from ..src import database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Thiam Zi Hui
class TestQuizController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_marking(self):
        request_mark = {
            "username": "edsheeran",
            "lessonCode": "X1010G1L2",
            "courseCode": "X1010",
            "classCode": "G1",
            "answer1": "Option3",
            "answer2": "F",
        }
        response = self.app.post("/api/gradeQuiz", json=request_mark)
        self.assertEqual(response.status_code, 200)
