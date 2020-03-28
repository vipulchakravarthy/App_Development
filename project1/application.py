'''
flask module to develop web Applciation
'''
from flask import Flask, render_template, request, session, redirect
from models import *
from flask_session import Session
import os
from sqlalchemy.exc import SQLAlchemyError

APP = Flask(__name__)

#Configure DB
APP.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(APP)

# Configure session to use filesystem
APP.config["SESSION_PERMANENT"] = False
APP.config["SESSION_TYPE"] = "filesystem"
Session(APP)

'''
This route is for home page
check if the user is logged or not
if not redirect to register
'''
@APP.route("/")
def index():
    if session.get("user_id") is None:
        return render_template('register.html', text="Please Login")
    return render_template("home.html", text="Welcome to Book Reviews")

'''
This route is for register page
'''
@APP.route("/register", methods=["GET", "POST"])
def register():
    message = ""
    if request.method == "POST":
        user_name = request.form.get("first_name")
        email = request.form.get("email")
        password = request.form.get("password")

        try:
            new_user = User(username=user_name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            message = "Registered successfully, Please Login"
            return render_template("success.html", text=message)

        except SQLAlchemyError as e:
            message = str(e.__dict__['orig'])
            return render_template("success.html", text=message)
    return render_template('register.html')

'''
This route is for authentication
'''
@APP.route("/auth", methods=["POST"])
def authentication():
    email = request.form.get("email")
    password = request.form.get("password")

    data = User.query.filter_by(email=email)
    if data[0].email == email and data[0].password == password:
        session["user_id"] = data[0].id
        session["user_name"] = data[0].username
        return render_template("home.html", text="Welcome to Book Reviews")

    return render_template("register.html", text="email or password is incorrect")

'''
This route is to logout
'''
@APP.route("/logout")
def logout():
    """ Log user out """
    # Forget any user ID
    session.clear()

    # Redirect user to login form
    return redirect("/register")

'''
This route is for printing all users
'''
@APP.route("/admin", methods=["GET"])
def fetch_users():
    data = User.query.order_by(User.created.desc()).all()
    return render_template('users.html', data=data)
