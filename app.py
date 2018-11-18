# 3p
from flask import Flask
from flask_restful import Api

# project
from config import Development
from models import db
from resources.status import Status
from resources.uptime import Uptime


app = Flask(__name__)
app.config.from_object(Development)
api = Api(app)
api_version = 'v1'
db.init_app(app)

api_url = 'api/{}'.format(api_version)
api.add_resource(Status, '/{}/status/<name>'.format(api_url))
api.add_resource(Uptime, '/{}/uptime/<name>'.format(api_url))

if __name__ == '__main__':
    app.run(debug=True)
