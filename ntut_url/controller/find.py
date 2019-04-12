from ..models.url import Url


def main(name: str):
    if Url.check_name(name):
        return Url(name).target
    else:
        return None
