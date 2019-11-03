from flask import Flask, jsonify

from extensions.db import db
from models.url import Url
from routes.api import app as api_route
from routes.redirect import app as redirect_route


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(redirect_route)

db.init_app(app)


@app.before_first_request
def init():
    db.create_all()


@app.route('/')
def root():
    return jsonify({
        'message': 'Hello World!'
    })


def main():
    app.run()


if __name__ == '__main__':
    main()
