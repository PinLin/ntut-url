from flask import Blueprint, redirect, abort

from models.url import Url


app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    url = Url.find(name)

    if not url:
        abort(404)

    return redirect(url.target, code=301)
