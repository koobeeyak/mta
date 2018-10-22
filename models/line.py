# project
from models import db


class Line(db.Model):
    name = db.Column(db.String(20), primary_key=True)
    status = db.Column(db.String(20))
    time_delayed = db.Column(db.Integer)

    def __init__(self, name, status, time_delayed):
        self.name = name
        self.status = status
        self.time_delayed = time_delayed
