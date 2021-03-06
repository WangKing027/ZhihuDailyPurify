import os
from flask import Flask

import controller

app = Flask(__name__)


@app.route("/")
def hello():
    return "Index"


@app.route("/news/<date>")
def feed_of_date(date):
    return controller.feed_of_date(date)


@app.route("/search/<keyword>")
def search(keyword):
    return controller.search(keyword)


if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(port=int(port))
