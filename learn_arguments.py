def func_arg(parameter, *args):
    print("parameter:", parameter)
    for arg in args:
        print("arg:", arg)


func_arg(1, 'aa', 'bb', 'cc')


def func_kwargs(parameter, **kwargs):
    print("parameter:", parameter)
    for key in kwargs:
        print("keyword arg: %s: %s" % (key, kwargs[key]))


func_kwargs(1, id=33, name='jack', city='shanghai', age='20')


def fun(parameter, *args, **kwargs):
    print("parameter:", parameter)
    for arg in args:
        print("arg:", arg)
    for key in kwargs:
        print("keyword arg: %s: %s" % (key, kwargs[key]))


fun(1, 'aa', 'bb', 'cc', id=33, name='jack', city='shanghai', age='20')
