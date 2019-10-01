from matplotlib import pyplot

import numpy


def lagrange(x, y, z):
    n = len(x)  # n = len(y)
    s = 0
    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (z - x[j]) / (x[i] - x[j])
        s = s + p * y[i]
    return s


if __name__ == '__main__':
    x = numpy.array([1., -1., 4., 5.])
    y = numpy.array([3, -3., 12., -2.])

    _x = numpy.linspace(-6., 10., 100)

    _y = [lagrange(x, y, z) for z in _x]

    pyplot.plot(x, y, 'bo')
    pyplot.plot(_x, _y, 'r--')
    pyplot.show()
    pyplot.savefig('lagrange.png')