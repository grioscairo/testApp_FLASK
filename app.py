from flask import Flask, render_template,request, flash

#Run on PS
#   $env:FLASK_APP = "app"
#   $env:FLASK_ENV = "development"
#   flask run

app = Flask(__name__)
app.secret_key = "asdf"

@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/greet", methods = ["POST", "GET"])
def greet():
    flash("Hi " + str(request.form ['name_input']) + ", great to see you!")
    return render_template("index.html")
    