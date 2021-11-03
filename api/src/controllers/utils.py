from flask import request, jsonify
import json
from bson import ObjectId
from datetime import datetime, date
from pprint import pprint
from src.database import mongo

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)