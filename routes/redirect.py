from flask import Blueprint, redirect, abort

from services.redirect import Redirect


app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    if Redirect.is_exist(name):
        target = Redirect.get_target(name)

        return redirect(target, code=301)
    else:
        abort(404)
