import unittest
from unittest.mock import patch
from mongomock import MongoClient
from src.app import create_app
import src.database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Jessie Ng
class TestQuestionController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(src.database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_addQuestions(self):
        request_questions = {
            "lessonCode": "X1010G1L1",
            "q1": "Question1",
            "options1": ["Option1", "Option2", "Option3", "Option4"],
            "answer1": "Option2",
            "q2": "Question2",
            "options2": ["Option1", "Option2", "Option3", "Option4"],
            "answer2": "Option4",
        }

        response_question = self.app.post(
            "/addQuestions", json=request_questions
        )
        self.assertEqual(response_question.status_code, 200)
