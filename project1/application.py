from flask import Flask, render_template, request
from models import *
from datetime import datetime as dt
import os

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

        data = User.query.filter_by(email=email).all()
        if len(data) > 0:
            message = "User already exists"
            return render_template("success.html", text = message)

        new_user = User(username= user_name, email= email, password = password, created=dt.now()) 
        db.session.add(new_user)
        db.session.commit()
        
        message = "Registered successfully, Please Login"

        return render_template("success.html", text = message)
    return render_template('register.html')


@app.route("/admin", methods=["GET"])
def fetch_users():
    data = User.query.all()
    print(data)
    return render_template('users.html', data=data)