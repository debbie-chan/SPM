import unittest
from unittest.mock import patch
from mongomock import MongoClient
from ..src.app import create_app
from ..src import database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Sheri Lee
class TestUserController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getAllUsers(self):
        response = self.app.get("/api")
        self.assertEqual(response.status_code, 200)

    def test_getAllOfRole(self):
        response_admin = self.app.get("/api/admin")
        response_trainer = self.app.get("/api/trainer")
        response_learner = self.app.get("/api/learner")
        self.assertEqual(response_admin.status_code, 200)
        self.assertEqual(response_trainer.status_code, 200)
        self.assertEqual(response_learner.status_code, 200)

    def test_getEnrolledLearners(self):
        response_valid = self.app.get("/api/getEnrolledLearners/X1010/G1")
        response_invalid = self.app.get("/api/getEnrolledLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getPendingLearners(self):
        response_valid = self.app.get("/api/getPendingLearners/X1010/G1")
        response_invalid = self.app.get("/api/getPendingLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getUnenrolledLearners(self):
        response_valid = self.app.get("/api/getUnenrolledLearners/X1010/G1")
        response_invalid = self.app.get("/api/getUnenrolledLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getOneUser(self):
        response_valid = self.app.get("/api/trainer/emilymariko")
        response_invalid = self.app.get("/api/trainer/bettyboop")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)


class TestAdminController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_assignTrainerToClass(self):
        response_valid = self.app.get(
            "/api/assignTrainerToClass/emilymariko/X2000/G1"
        )
        response_invalid = self.app.get(
            "/api/assignTrainerToClass/emilymariko/X2000"
        )
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_verifyLearner(self):
        response_valid = self.app.get("/api/verifyLearner/emmajones/X7845/G1")
        response_invalid = self.app.get("/api/verifyLearner/emmajones/X100/G1")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 500)

    def test_assignLearnerToClass(self):
        response_valid = self.app.get(
            "/api/assignLearnerToClass/emmajones/X1010/G1"
        )
        response_invalid = self.app.get(
            "/api/assignLearnerToClass/emmajones/X100"
        )
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)


class TestLearnerController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_addPendingCourse(self):
        response_valid = self.app.get(
            "/api/addPendingCourse/emmajones/X2000/G1"
        )
        response_invalid = self.app.get(
            "/api/addPendingCourse/emmajones/X2000"
        )
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_deletePendingCourse(self):
        response_valid = self.app.get(
            "/api/deletePendingCourse/emmajones/X2000/G1"
        )
        response_invalid = self.app.get(
            "/api/deletePendingCourse/emmajones/X2000"
        )
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)
