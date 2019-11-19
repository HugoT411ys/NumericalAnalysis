import numpy

from matplotlib import pyplot
from Polynomial_Interpolation.lagrange import *


def monte_carlo(x1, x2, n_points, function):
    y = numpy.random.uniform(0., 1., n_points)
    y = function(x1 + (x2 - x1) * y)
    return ((x2 - x1) / n_points) * sum(y)


def main():
    n = 100000
    a, b = 3., 5.

    def f(x): return numpy.exp(-x**2)

    i = monte_carlo(x1=a, x2=b, n_points=n, function=f)

    print(i)


if __name__ == '__main__':
    main()
