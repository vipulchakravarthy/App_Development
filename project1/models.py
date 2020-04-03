'''
this file is for models in our database
'''
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt

#create a db instance
db = SQLAlchemy()

'''
Class for storing user details
'''
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

<<<<<<< HEAD
'''
Class for storing book details
'''
=======


>>>>>>> Authentication
class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer,
                   primary_key=True)
    isbn = db.Column(db.String(80),
                         index=False,
                         unique=True,
                         nullable=False)
    title = db.Column(db.String(80),
                      index=True,
                      unique=False,
                      nullable=False)
    author = db.Column(db.String(128))
    year = db.Column(db.Integer,
                        index=False,
                        unique=False,
                        nullable=False)

    def __init__(self, isbn, title, author, year) :
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return self.title