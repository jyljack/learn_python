from functools import reduce

func = lambda x: x * 2

print(func)
print(func(2))

# filter(function, sequence)
foo = filter(lambda x: x % 2 == 0, range(10))
print(list(foo))

# map(function,iterable1,iterable2)
foo = map(lambda x, y: (x + y) + 2, range(10), range(10))
print(list(foo))

# reduce（function，iterable)
foo = reduce(lambda x, y: x + y, range(10))
print(foo)
