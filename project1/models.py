from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(128))
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __init__(self, username, email, password) :
        self.username = username
        self.email = email
        self.password = password
        self.created = dt.now()

    def __repr__(self):
        return self.email