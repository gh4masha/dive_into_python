#decorator that tranforms the result of functions to json

import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped

@to_json
def get_data():
    return 42


print (get_data())  # вернёт '{"data": 42}'
print (get_data.__name__)  # вернёт '{"data": 42}'