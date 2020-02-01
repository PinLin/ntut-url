from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS
import random
import string

from extensions.db import db
from models.url import Url
from services.urls import UrlsService


app = Blueprint('urls', __name__)
CORS(app)


@app.route('/', methods=['POST'])
def post_urls():
    data = request.json
    name = data.get('name')
    target = data.get('target')

    # 如果 name 已經被使用
    if UrlsService.is_exist(name):
        abort(409)

    result = UrlsService.create_new_url(name, target)

    return jsonify({
        'result': result,
    })
