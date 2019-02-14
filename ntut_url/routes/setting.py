import sys
from flask import Blueprint, request, abort, jsonify, send_from_directory
from ..api.setting import browse, create

api = Blueprint('setting', __name__)


@api.route('/', defaults={'filename': None}, methods=['GET'])
@api.route('/<filename>', methods=['GET'])
def setting(filename: str):
    if not filename:
        filename = 'index.html'
    return send_from_directory(sys.path[0] + '/ntut_url/pages', filename)


@api.route('/browse', methods=['GET'])
def setting_browse():
    secret = request.headers.get('Secret')

    code, response = browse.main(secret)

    if code == 200:
        return jsonify(response)

    else:
        return abort(code)


@api.route('/create', methods=['POST'])
def setting_create():
    secret = request.headers.get('Secret')
    data = request.json

    code, response = create.main(secret, data)

    if code == 201:
        return jsonify(response)

    else:
        return abort(code)
