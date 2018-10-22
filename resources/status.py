# 3p
from flask_restful import Resource

# project
from models.line import Line


class Status(Resource):
    def get(self, name):
        return {
            "line": name,
            "status": Line.query.get(name),
        }
