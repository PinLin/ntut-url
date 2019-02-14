from ...models.url import Url
from ...config import SECRET


def main(secret: str, data: dict):
    if secret != SECRET['code']:
        return 401, None

    name = data['name']
    target = data['target']

    if Url.is_exist(name):
        return 403, None

    if not '://' in target:
        target = 'http://' + target

    Url.create(name, target)

    url = Url(name)
    result = {
        'name': url.name,
        'target': url.target,
    }

    return 201, {
        'result': result,
    }
