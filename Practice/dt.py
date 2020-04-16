import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    now_date = now.month == 4 and now.day == 16
    return render_template("index1.html", now_date=now_date)