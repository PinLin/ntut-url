from flask import Blueprint, request, abort, jsonify
from ..controller.create import main as create

app = Blueprint('setting', __name__)


@app.route('/create', methods=['POST'])
def create_route():
    data = request.json
    name = data.get('name')
    target = data.get('target')

    response = create(name, target)

    if response:
        return jsonify(response)

    else:
        return abort(403)
