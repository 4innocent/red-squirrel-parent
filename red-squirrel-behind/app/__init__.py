from conf import Conf
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """ 创建app """
    app = Flask(__name__)
    app.config.from_object(Conf)
    # 解决cors跨域问题
    CORS(app)
    # 注册sqlalchemy管理数据库
    db.init_app(app)
    # migreate
    migrate.init_app(app)
    return app
