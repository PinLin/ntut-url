from flask import Blueprint, redirect, abort

from controller.find import main as find


app = Blueprint('redirect', __name__)


@app.route('/', methods=['GET'])
def root_route():
    return redirect('/static/index.html', code=302)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    target = find(name)

    if target:
        return redirect(target, code=301)

    else:
        return abort(404)
