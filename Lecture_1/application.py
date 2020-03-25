from flask import Flask, render_template, request # Import the class `Flask` from the `flask` module, written by someone else.
import datetime

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
  return render_template("index.html")

@app.route("/more")
def more():
	return render_template("more.html")


@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name") 
    # take the request the user made, access the form,
    # and store the field called `name` in a Python variable also called `name`
    return render_template("hello.html", name=name)