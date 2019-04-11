from flask import Blueprint, redirect, abort
from ..controller.get_url import main as get_url

app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    code, target = get_url(name)

    if code // 100 == 3:
        return redirect(target, code=code)

    else:
        return abort(code)
