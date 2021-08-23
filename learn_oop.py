class DataSet(object):
    def __init__(self):
        self._images = 1
        self._labels = 2

    @property
    def images(self):  # 方法加入@property后，这个方法相当于一个属性，这个属性可以让用户进行使用，而且用户有没办法随意修改。
        return self._images

    @property
    def labels(self):
        return self._labels


l = DataSet()
print(l.images)


# @staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
# @classmethod 也不需要self参数，但第一个参数需要是表示自身类的cls参数。
class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        cls().foo()


a = A()
a.foo()
A.static_foo()
A.class_foo()



