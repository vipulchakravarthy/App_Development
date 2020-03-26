from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "Users"
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

    def __init__(self, username, email, password, created) :
        self.username = username
        self.email = email
        self.password = password
        self.created = created