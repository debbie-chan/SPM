import unittest
from unittest.mock import patch
from mongomock import MongoClient
from src.app import create_app
import src.database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


# Led By: Sheri Lee
class TestUserController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(src.database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_getAllUsers(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

    def test_getAllOfRole(self):
        response_admin = self.app.get("/admin")
        response_trainer = self.app.get("/trainer")
        response_learner = self.app.get("/learner")
        self.assertEqual(response_admin.status_code, 200)
        self.assertEqual(response_trainer.status_code, 200)
        self.assertEqual(response_learner.status_code, 200)

    def test_getEnrolledLearners(self):
        response_valid = self.app.get("/getEnrolledLearners/X1010/G1")
        response_invalid = self.app.get("/getEnrolledLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getPendingLearners(self):
        response_valid = self.app.get("/getPendingLearners/X1010/G1")
        response_invalid = self.app.get("/getPendingLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getUnenrolledLearners(self):
        response_valid = self.app.get("/getUnenrolledLearners/X1010/G1")
        response_invalid = self.app.get("/getUnenrolledLearners/X1010")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_getOneUser(self):
        response_valid = self.app.get("/trainer/emilymariko")
        response_invalid = self.app.get("/trainer/bettyboop")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_createUser(self):
        request_admin = {
            "employeeName": "Sally Loh",
            "designation": "Admin Manager",
            "department": "Human Resources",
            "username": "sallyloh",
            "password": "password",
            "role": "admin",
        }
        request_trainer = {
            "department": "Technology",
            "designation": "Senior Engineer",
            "employeeName": "Emily Mariko",
            "password": "password",
            "role": "trainer",
            "trainedCourses": {"X100": "G1"},
            "trainingCourses": {"X1010": "G1"},
            "username": "emilymariko",
        }
        request_learner = {
            "attemptedCourses": {"X200": "G1"},
            "completedCourses": {"X100": "G1"},
            "department": "Technology",
            "designation": "Junior Engineer",
            "employeeName": "Emma Jones",
            "enrolledCourses": {"X1010": "G1"},
            "password": "password",
            "quizResults": {},
            "role": "learner",
            "username": "emmajones",
        }

        response_admin = self.app.post("/createUser", json=request_admin)
        response_trainer = self.app.post("/createUser", json=request_trainer)
        response_learner = self.app.post("/createUser", json=request_learner)
        self.assertEqual(response_admin.status_code, 201)
        self.assertEqual(response_trainer.status_code, 201)
        self.assertEqual(response_learner.status_code, 201)

        response_admin_json = response_admin.get_json()
        response_trainer_json = response_trainer.get_json()
        response_learner_json = response_learner.get_json()
        expected_admin_json = {
            "_id": response_admin_json["_id"],
            "employeeName": "Sally Loh",
            "designation": "Admin Manager",
            "department": "Human Resources",
            "username": "sallyloh",
            "password": "password",
            "role": "admin",
        }
        expected_trainer_json = {
            "_id": response_trainer_json["_id"],
            "department": "Technology",
            "designation": "Senior Engineer",
            "employeeName": "Emily Mariko",
            "password": "password",
            "role": "trainer",
            "trainedCourses": {"X100": "G1"},
            "trainingCourses": {"X1010": "G1"},
            "username": "emilymariko",
        }
        expected_learner_json = {
            "_id": response_learner_json["_id"],
            "attemptedCourses": {"X200": "G1"},
            "completedCourses": {"X100": "G1"},
            "department": "Technology",
            "designation": "Junior Engineer",
            "employeeName": "Emma Jones",
            "enrolledCourses": {"X1010": "G1"},
            "password": "password",
            "quizResults": {},
            "role": "learner",
            "username": "emmajones",
        }
        self.assertEqual(response_admin_json, expected_admin_json)
        self.assertEqual(response_trainer_json, expected_trainer_json)
        self.assertEqual(response_learner_json, expected_learner_json)


# Led By: Deborah Chan
class TestAdminController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(src.database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_assignTrainerToClass(self):
        response_valid = self.app.get(
            "/assignTrainerToClass/emilymariko/X2000/G1"
        )
        response_invalid = self.app.get(
            "/assignTrainerToClass/emilymariko/X2000"
        )
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_verifyLearner(self):
        response_valid = self.app.get("/verifyLearner/emmajones/X7845/G1")
        response_invalid = self.app.get("/verifyLearner/emmajones/X100/G1")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 500)

    def test_assignLearnerToClass(self):
        response_valid = self.app.get(
            "/assignLearnerToClass/emmajones/X1010/G1"
        )
        response_invalid = self.app.get("/assignLearnerToClass/emmajones/X100")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)


# Led By: Deborah Chan
class TestLearnerController(unittest.TestCase):
    def setUp(self):
        self.patcher = patch.object(src.database, "mongo", PyMongoMock())
        self.app = create_app(
            "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK"
            "@clusterlms.k10xd.mongodb.net/lms"
        ).test_client()

    def tearDown(self):
        self.patcher = None
        self.app = None

    def test_addPendingCourse(self):
        response_valid = self.app.get("/addPendingCourse/emmajones/X2000/G1")
        response_invalid = self.app.get("/addPendingCourse/emmajones/X2000")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_deletePendingCourse(self):
        response_valid = self.app.get(
            "/deletePendingCourse/emmajones/X2000/G1"
        )
        response_invalid = self.app.get("/deletePendingCourse/emmajones/X2000")
        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)
