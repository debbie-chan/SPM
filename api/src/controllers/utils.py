import json
from bson import ObjectId
from datetime import datetime, date


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


class DatetimeConverter:
    def strToDatetime(o):
        return datetime.strptime(o["$date"], "%Y-%m-%dT%H:%M:%S.000Z")
