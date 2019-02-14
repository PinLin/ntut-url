from flask import Blueprint, request, jsonify
from ..api.setting import browse, create

api = Blueprint('setting', __name__)


@api.route('/browse', methods=['GET'])
def setting_browse():
    return jsonify(browse.main())


@api.route('/create', methods=['GET'])
def setting_create():
    return jsonify(create.main())
