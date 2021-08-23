# https://docs.python.org/zh-cn/3/library/abc.html

import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def say(self):
        raise NotImplementedError


class Dog(Animal):
    def __init__(self):
        pass

    def say(self):
        print("Wang Wang")


class Cat(Animal):
    def __init__(self):
        pass

    def say(self):
        print("Miao Miao")


dog = Dog()
dog.say()
cat = Cat()
cat.say()
