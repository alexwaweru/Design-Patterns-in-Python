class Singleton(object):
    __instance = None

    def __new__(cls, val):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
            Singleton.__instance.val = val
        return Singleton.__instance


class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'My name is %s' % self.name


person1 = Singleton(Person('Alex'))
person2 = Singleton(Person('Peter'))
person3 = Singleton(Person('John'))
person4 = Singleton(Person('Doe'))
print(person1.val)
print(person2.val)
print(person3.val)
print(person4.val)


