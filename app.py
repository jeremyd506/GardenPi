from flask import Flask, render_template   
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/moisture")
def moisture():
    return render_template("moisture.html")

@app.route("/watering")
def watering():
    return render_template("watering.html")