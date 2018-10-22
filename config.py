# std
import os


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://localhost/mta"  # os.environ['DATABASE_URL']


class Production(Config):
    pass


class Development(Config):
    DEVELOPMENT = True
    DEBUG = True
