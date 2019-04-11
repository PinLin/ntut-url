from ...models.url import Url


def main():
    results = []
    for url in Url.find_all():
        results.append({
            'name': url.name,
            'target': url.target,
        })

    return 200, {
        'results': results,
    }
