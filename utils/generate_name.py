import random
import string


def generate_name(length: int):
    result = ''

    choices = string.ascii_letters + string.digits
    for _ in range(length):
        result += random.choice(choices)

    return result
