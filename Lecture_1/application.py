from flask import Flask, render_template, request, session # Import the class `Flask` from the `flask` module, written by someone else.
import datetime

from flask_session import Session # an additional extension to sessions which allows them
                                  # to be stored server-side

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("notes") is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)

    return render_template("index.html", notes=session["notes"])


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name") 
    # take the request the user made, access the form,
    # and store the field called `name` in a Python variable also called `name`
    return render_template("hello.html", name=name)