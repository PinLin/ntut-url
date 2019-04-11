import sys
from flask import Blueprint, request, abort, jsonify
from ..controller.setting import create

api = Blueprint('setting', __name__)


@api.route('/create', methods=['POST'])
def setting_create():
    data = request.json
    name = data['name']
    target = data['target']

    code, response = create.main(name, target)

    if code == 201:
        return jsonify(response)

    else:
        return abort(code)
