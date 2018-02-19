# FunctionObjects/StrategyPattern.py


# The strategy interface:
class FindMinima:
    # Line is a sequence of points:
    def algorithm(self, line_):
        pass


# The various strategies:
class LeastSquares(FindMinima):

    def algorithm(self, line_):
        return [1.1, 2.2]  # Dummy


class NewtonsMethod(FindMinima):
    
    def algorithm(self, line_):
        return [3.3, 4.4]  # Dummy


class Bisection(FindMinima):
    
    def algorithm(self, line_):
        return [5.5, 6.6]  # Dummy


class ConjugateGradient(FindMinima):
    
    def algorithm(self, line_):
        return [3.3, 4.4]  # Dummy


# The "Context" controls the strategy:
class MinimaSolver:

    def __init__(self, strategy):
        self.strategy = strategy

    def minima(self, line):
        return self.strategy.algorithm(line)

    def change_algorithm(self, newAlgorithm):
        self.strategy = newAlgorithm


solver = MinimaSolver(LeastSquares())
line = [1.0, 2.0, 1.0, 2.0, -1.0, 3.0, 4.0, 5.0, 4.0]
print(solver.minima(line))
solver.change_algorithm(Bisection())
print(solver.minima(line))
