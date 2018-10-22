# 3p
from flask_restful import Resource

# project
from common.utils import get_uptime
from models.line import Line

# todo import metric that shows lifetime of the app, convert to minutes. this global is just a placeholder
total_time = 9999


class Uptime(Resource):
    def get(self, name):
        line = Line.query.get(name)
        uptime = get_uptime(line.time_delayed, total_time)
        return {
            "line": name,
            "uptime": uptime,
        }
