from conf import Conf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    """ 创建app """
    app = Flask(__name__)
    app.config.from_object(Conf)
    CORS(app)
    return app
