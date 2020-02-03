from flask import Blueprint, redirect, abort

from services.redirect import RedirectService
from services.urls import UrlsService


app = Blueprint('redirect', __name__)


@app.route('/<name>', methods=['GET'])
def redirect_route(name: str):
    if UrlsService.is_exist(name) and not UrlsService.is_expired(name):
        RedirectService.click_url(name)

        target = RedirectService.get_target(name)

        return redirect(target, code=301)
    else:
        abort(404)
