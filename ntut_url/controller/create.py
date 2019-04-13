import random
import string
from ..models.url import Url


def main(name: str, target: str):
    if name:
        if Url.check_name(name):
            return None
    else:
        while True:
            name = ''.join(random.choice(string.ascii_letters +
                                         string.digits) for x in range(6))
            if not Url.check_name(name):
                break

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
