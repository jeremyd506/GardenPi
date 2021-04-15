from flask import Flask, render_template
import datetime
from gpiozero import MCP3008
from decimal import *

app = Flask(__name__)

@app.route("/")
def home():
  currenttime = gettime()
  templateData = {
    'time' : currenttime
  }
  return render_template("home.html", **templateData)

@app.route("/about")
def about():
    return render_template("about.html",)

@app.route("/moisture")
def moisture():
    currenttime = gettime()
    read = MCP3008(channel=0)
    decimalread = Decimal(read.value)
    water = Decimal(.55)
#   print "decimal read is", decimalread
#   print "water is ", water
#   print "compare value is" , decimalread.compare(water)
    percent =  str(round(decimalread*100,2))
#   print percent
    if decimalread.compare(water) == -1:
      moisture = "No water needed. Soil is, {}% dry".format(percent)
    elif decimalread.compare(water) == 1:
      moisture = "Time to water. Soil is, {}% dry".format(percent)
    templateData = {
       'moisture' : moisture, 
       'time' : currenttime
    }
    return render_template("moisture.html", **templateData)

@app.route("/watering")
def watering():
    return render_template("watering.html")

def gettime():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    return(timeString)


if __name__ == '__main__':
  app.run(debug=True, port=80, host='0.0.0.0')
