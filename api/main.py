from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

import json
import certifi
from bson import json_util
from pprint import pprint
from datetime import datetime

app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK@clusterlms.k10xd.mongodb.net/lms"
mongo = PyMongo(app, tlsCAFile=certifi.where())
userdb = mongo.cx["user"]
coursedb = mongo.cx["course"]
