from flask import Blueprint, request, abort, jsonify
from ..controller.create_url import main as create_url

app = Blueprint('setting', __name__)


@app.route('/create', methods=['POST'])
def create_route():
    data = request.json
    name = data['name']
    target = data['target']

    code, response = create_url(name, target)

    if code == 201:
        return jsonify(response)

    else:
        return abort(code)
