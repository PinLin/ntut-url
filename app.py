import os
import sys
from flask import Flask

from models.url import Url
from routes.api import app as api_route
from routes.redirect import app as redirect_route


Url.create_table()

app = Flask(__name__)
app.static_folder = 'static/ntut_url_client'
app.register_blueprint(api_route, url_prefix='/api')
app.register_blueprint(redirect_route)


def main():
    SERVER_PORT = int(os.environ.get('SERVER_PORT') or 5000)

    app.run(port=SERVER_PORT, threaded=True)


if __name__ == '__main__':
    main()
