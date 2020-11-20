from home import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for


class BaseModel:
    create_time = db.Column(db.Date, default=datetime.now)
    cupdate_time = db.Column(db.Date, default=datetime.now, onupdate=datetime.now)


class User(db.Model):
    name = db.Column()
