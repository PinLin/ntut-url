from flask import Flask
from .models.url import Url
from .routes.setting import api as setting_api
from .routes.redirect import api as redirect_api

Url.create_table()

app = Flask(__name__)
app.register_blueprint(setting_api, url_prefix='/api')
app.register_blueprint(redirect_api)
