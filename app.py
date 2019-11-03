from flask import Flask, jsonify

from models.url import Url
from routes.api import app as api_route
from routes.redirect import app as redirect_route


Url.create_table()

app = Flask(__name__)
app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(redirect_route)


@app.route('/')
def root():
    return jsonify({
        'message': 'Hello World!'
    })


def main():
    app.run()


if __name__ == '__main__':
    main()
