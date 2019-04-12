from ..models.url import Url


def main(name: str, target: str):
    if Url.is_exist(name):
        return None

    if not '://' in target:
        target = 'http://' + target

    Url.create(name, target)

    url = Url(name)
    result = {
        'name': url.name,
        'target': url.target,
    }

    return {
        'result': result,
    }
