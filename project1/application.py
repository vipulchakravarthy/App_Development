from flask import Flask, render_template, request, session, redirect
from models import *
from flask_session import Session
import os
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

#Configure DB
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    if session.get("user_id") is None:
        return render_template('register.html', text ="Please Login")
    return render_template("home.html", text="Welcome to Book Reviews")

@app.route("/register",methods=["GET","POST"])
def register():
    message = ""
    if request.method == "POST":
        user_name = request.form.get("first_name")
        email = request.form.get("email")
        password = request.form.get("password")

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

@app.route("/auth", methods=["POST"])
def authentication():
    email = request.form.get("email")
    password = request.form.get("password")

    data = User.query.filter_by(email=email)
    if data[0].email == email and data[0].password == password:
        session["user_id"] = data[0].id
        session["user_name"] = data[0].username
        return render_template("home.html", text="Welcome to Book Reviews")

    return render_template("register.html", text="email or password is incorrect")

@app.route("/logout")
def logout():
    """ Log user out """

    # Forget any user ID
    session.clear()

    # Redirect user to login form
    return redirect("/register")

@app.route("/admin", methods=["GET"])
def fetch_users():
    data = User.query.all()
    return render_template('users.html', data=data)