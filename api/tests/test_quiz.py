import unittest
from unittest.mock import patch
from mongomock import MongoClient
from ..src.app import create_app
from ..src import database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Jessie Ng / Thiam Zi Hui
class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getQuiz(self):
        response = self.app.get("/api/getQuiz/X1010G1L1")
        self.assertEqual(response.status_code, 200)
