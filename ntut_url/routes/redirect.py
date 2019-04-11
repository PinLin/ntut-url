from flask import Blueprint, redirect, abort
from ..controller.redirect import process

app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    code, target = process.main(name)

    if code // 100 == 3:
        return redirect(target, code=code)

    else:
        return abort(code)
