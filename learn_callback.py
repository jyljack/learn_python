def my_callback(args):
    print(*args)


def caller(args, func):
    func(args)


caller((1, 2), my_callback)
