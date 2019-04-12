from ..models.url import Url


def main(name: str):
    if Url.is_exist(name):
        return Url(name).target
    else:
        return None
