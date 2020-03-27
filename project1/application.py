from flask import Flask, render_template, request
from models import *
import os
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=["GET","POST"])
def register():
    message = ""
    if request.method == "POST":
        user_name = request.form.get("first_name")
        email = request.form.get("email")
        password = request.form.get("password")

        # data = User.query.filter_by(email=email).all()
        # if len(data) > 0:
        #     message = "User already exists"
        #     
        try:
            new_user = User(username= user_name, email= email, password = password) 
            db.session.add(new_user)
            db.session.commit()
            message = "Registered successfully, Please Login"
            return render_template("success.html", text = message)

        except SQLAlchemyError as e:
            message = str(e.__dict__['orig'])
            return render_template("success.html", text = message)
        
    return render_template('register.html')


@app.route("/admin", methods=["GET"])
def fetch_users():
    data = User.query.all()
    return render_template('users.html', data=data)