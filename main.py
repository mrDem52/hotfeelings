from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from config import settings
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/create-article', methods=['POST', 'GET'])
def create_article():
    if request.method == "POST":
        pass
    else:
        return render_template("create-article.html")


if __name__ == "__main__":
    app.run(debug=True)
