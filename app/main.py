from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://dbAdmin:Ve08ByJJOk5RNhWK@clusterlms.k10xd.mongodb.net/course?retryWrites=true&w=majority"
mongo = PyMongo(app)
userdb = mongo.cx["user"]
coursedb = mongo.cx["course"]
