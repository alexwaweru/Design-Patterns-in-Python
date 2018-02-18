class DrinkComponent:

    def get_description(self):
        return self.__class__.__name__

    def get_total_cost(self):
        return self.__class__.cost


class Mug(DrinkComponent):
    cost = 0.0


class Decorator(DrinkComponent):

    def __init__(self, drink_component):
        self.component = drink_component

    def get_total_cost(self):
        return self.component.get_total_cost() + \
          DrinkComponent.get_total_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ' + DrinkComponent.get_description(self)


class Espresso(Decorator):
    cost = 0.75

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


class Decaf(Decorator):
    cost = 0.0

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


class FoamedMilk(Decorator):
    cost = 0.25

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


class SteamedMilk(Decorator):
    cost = 0.25

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


class Whipped(Decorator):
    cost = 0.25

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


class Chocolate(Decorator):
    cost = 0.25

    def __init__(self, drink_component):
        Decorator.__init__(self, drink_component)


cappuccino = Espresso(FoamedMilk(Mug()))
print(cappuccino.get_description().strip() + ": $%3.3f" % cappuccino.get_total_cost())

cafeMocha = Espresso(SteamedMilk(Chocolate(Whipped(Decaf(Mug())))))

print(cafeMocha.get_description().strip() + ": $%3.3f" % cafeMocha.get_total_cost())
