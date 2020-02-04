from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS
import random
import string

from extensions.db import db
from models.url import Url
from services.urls import UrlsService


app = Blueprint('urls', __name__)
CORS(app)


@app.route('/', methods=['POST'], strict_slashes=False)
def post_urls():
    data = request.json
    name = data.get('name')
    target = data.get('target')
    expire_seconds = data.get('expireSeconds')

    # 如果 name 已經被使用且尚未過期
    if UrlsService.is_exist(name):
        if not UrlsService.is_expired(name):
            abort(409)

    result = UrlsService.create_url(name, target, expire_seconds)

    return jsonify({
        'result': result,
    })
