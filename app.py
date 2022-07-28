# Entry point for the application.
import json
from random import randint

from datetime import datetime

from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/hello/")

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/api/QuoteoftheDay")
def random_question():
    with open('static/data.json') as quotesfile:
        data = json.load(quotesfile)
        qs = data["quotes"]
        random_index = randint(0, len(qs)-1)
        return qs[random_index]


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
