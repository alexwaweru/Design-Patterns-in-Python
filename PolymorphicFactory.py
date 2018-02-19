from __future__ import generators
import random


class ShapeFactory:
    factories = {}

    def add_factory(id, shapeFactory):
        ShapeFactory.factories.put[id] = shapeFactory
    addFactory = staticmethod(add_factory)

    # A Template Method:
    def create_shape(id):
        if not ShapeFactory.factories.has_key(id):
            ShapeFactory.factories[id] = eval(id + '.Factory()')
        return ShapeFactory.factories[id].create()
    createShape = staticmethod(create_shape)


class Shape(object):
    pass


class Circle(Shape):

    def draw(self):
        print("Circle.draw")

    def erase(self):
        print("Circle.erase")

    class Factory:

        def create(self):
            return Circle()


class Square(Shape):

    def draw(self):
        print("Square.draw")

    def erase(self):
        print("Square.erase")

    class Factory:

        def create(self):
            return Square()


def shape_name_gen(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ ShapeFactory.createShape(i)
           for i in shape_name_gen(7)]

for shape in shapes:
    shape.draw()
    shape.erase()
