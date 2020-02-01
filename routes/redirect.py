from flask import Blueprint, redirect, abort

from services.redirect import RedirectService


app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    if RedirectService.is_exist(name):
        target = RedirectService.get_target(name)

        return redirect(target, code=301)
    else:
        abort(404)
