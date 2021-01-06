from conf import Conf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """ 创建app """
    app = Flask(__name__)
    app.config.from_object(Conf)
    db.init_app(app)

    return app
