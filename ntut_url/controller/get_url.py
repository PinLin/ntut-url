from ..models.url import Url


def main(name: str):
    if Url.is_exist(name):
        return 301, Url(name).target
    else:
        return 404, None
