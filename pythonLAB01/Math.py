def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Person's name {} Age{}". format(self.name, self.age)