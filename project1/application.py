import os

from flask import Flask, session, request, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"

@app.route("/register",methods=["GET","POST"])
def register():
    register_message =""
    if request.method == "POST":
        email=request.form.get('email') 
        userPassword=request.form.get('password')
        data=db.execute("SELECT email FROM users").fetchall()
        for i in range(len(data)):
            if data[i]["email"]==email:
                register_message="email already exist"
                return render_template('success.html',text=register_message)
        db.execute("INSERT INTO users (email,password) VALUES (:a,:b)",{"a":email,"b":userPassword})
        db.commit()
        register_message="Success! You can log in now."
        return render_template('success.html', text =register_message)

    return render_template('register.html')


@app.route("/admin", methods=["GET"])
def fetch_users():
    data=db.execute("SELECT * FROM users").fetchall()
    return render_template('users.html', data=data)