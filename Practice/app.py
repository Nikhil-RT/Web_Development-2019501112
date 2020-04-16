# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     headline = "Hello, World!"
#     return render_template ("index.html", headline = headline)

# @app.route("/<string:name>")
# def hello(name):
#     headline = f"hello, {name}!"
#     return  render_template ("index.html", headline = headline)


# import datetime

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     now = datetime.datetime.now()
#     now_date = now.month == 4 and now.day == 16
#     return render_template("index1.html", now_date=now_date)

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     names = ["Nikhil","Ravi","Teja"]
#     return render_template("index2.html", names = names)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)