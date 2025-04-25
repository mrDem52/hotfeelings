from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:q@localhost/hf'
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nulllable=False)
    intro = db.Column(db.String(300), nulllable=False)
    text = db.Column(db.Text, nulllable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def user():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
