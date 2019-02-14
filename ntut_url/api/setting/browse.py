from ...models.url import Url
from ...config import SECRET


def main(secret: str):
    if secret != SECRET['code']:
        return 403, None

    result = []
    for url in Url.find_all():
        result.append({
            'name': url.name,
            'target': url.target,
        })

    return 200, {
        'result': result,
    }
