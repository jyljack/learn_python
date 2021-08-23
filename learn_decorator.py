from functools import wraps


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))
        return func(*args, **kwargs)
    return wrapper


@log
def test(param):
    print(test.__name__ + " param: " + param)


test("I'm a param")
