from flask import Blueprint, redirect, abort
from ..controller.redirect import process

api = Blueprint('redirect', __name__)


@api.route('/<name>', methods=['GET'])
def redirect_process(name: str):
    code, target = process.main(name)

    if code // 100 == 3:
        return redirect(target, code=code)

    else:
        return abort(code)
