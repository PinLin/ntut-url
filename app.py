from flask import Flask, redirect

from config import SQLALCHEMY_DATABASE_URI
from extensions.db import db
from models.url import Url
from routes.urls import app as urls_route
from routes.redirect import app as redirect_route


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(urls_route, url_prefix='/api/urls')
app.register_blueprint(redirect_route)

db.init_app(app)


@app.before_first_request
def init():
    db.create_all()


@app.route('/')
def root():
    return "Welcome to ntut-url!"


def main():
    app.run()


if __name__ == '__main__':
    main()
