from flask import Blueprint, request, abort, jsonify
from flask_cors import CORS
import random
import string

from extensions.db import db
from models.url import Url


app = Blueprint('urls', __name__)
CORS(app)


@app.route('/', methods=['POST'])
def post_urls():
    data = request.json
    name = data.get('name')
    target = data.get('target')

    # 如果 name 已經被使用
    if name and Url.find(name):
        abort(409)

    # 如果沒有給 name
    if not name:
        # 隨機產生 name
        while True:
            name = ''.join(random.choice(string.ascii_letters +
                                         string.digits) for x in range(6))
            if not Url.find(name):
                break

    # 沒有指明協定就加上 http://
    if not '://' in target:
        target = 'http://' + target

    # 建立縮網址
    url = Url.create(name, target)

    db.session.add(url)
    db.session.commit()

    result = {
        'name': url.name,
        'target': url.target,
    }

    return jsonify({
        'result': result,
    })
