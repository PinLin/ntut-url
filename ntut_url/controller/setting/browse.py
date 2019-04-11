from ...models.url import Url
from ...config import SECRET


def main(secret: str):
    if secret != SECRET['code']:
        return 401, None

    results = []
    for url in Url.find_all():
        results.append({
            'name': url.name,
            'target': url.target,
        })

    return 200, {
        'results': results,
    }
