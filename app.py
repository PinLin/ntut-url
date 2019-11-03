from flask import Flask

from models.url import Url
from routes.api import app as api_route
from routes.redirect import app as redirect_route


Url.create_table()

app = Flask(__name__)
app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(redirect_route)


def main():
    app.run()


if __name__ == '__main__':
    main()
