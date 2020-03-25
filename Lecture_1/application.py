from flask import Flask, render_template # Import the class `Flask` from the `flask` module, written by someone else.

app = Flask(__name__) # Instantiate a new web application called `app`, with `__name__` representing the current file

@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
  name = "Vipul"
  return render_template("index.html", Name=name)
