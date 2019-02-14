from flask import Blueprint, request, abort, jsonify
from ..api.setting import browse, create

api = Blueprint('setting', __name__)


@api.route('/browse', methods=['GET'])
def setting_browse():
    secret = request.args.get('secret')

    code, response = browse.main(secret)

    if code == 200:
        return jsonify(response)

    else:
        return abort(code)


@api.route('/create', methods=['GET'])
def setting_create():
    return jsonify(create.main())
