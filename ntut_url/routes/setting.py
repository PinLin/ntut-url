import sys
from flask import Blueprint, request, abort, jsonify
from ..controller.setting import create

app = Blueprint('setting', __name__)


@app.route('/create', methods=['POST'])
def create_route():
    data = request.json
    name = data['name']
    target = data['target']

    code, response = create.main(name, target)

    if code == 201:
        return jsonify(response)

    else:
        return abort(code)
