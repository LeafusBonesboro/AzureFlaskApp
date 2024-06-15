import json

from flask_restful import Resource

with open("profiles.json", "r") as f:
    db = json.load(f)
class ProfileResource(Resource):
    def get(self):
        return sorted(db, key=lambda x: x["last_name"])