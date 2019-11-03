from models.url import Url


def main(name: str):
    if Url.find(name):
        return Url.find(name).target
    else:
        return None
