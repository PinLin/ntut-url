from flask import Blueprint, jsonify
from ..api.redirect import process

api = Blueprint('redirect', __name__)


@api.route('/<name>', methods=['GET'])
def redirect_process(name: str):
    return jsonify(process.main(name))
