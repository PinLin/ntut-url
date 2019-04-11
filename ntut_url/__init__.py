from flask import Flask
from .models.url import Url
from .routes.setting import app as setting_route
from .routes.redirect import app as redirect_route

Url.create_table()

app = Flask(__name__)
app.register_blueprint(setting_route, url_prefix='/api')
app.register_blueprint(redirect_route)
