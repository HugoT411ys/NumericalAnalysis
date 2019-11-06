import numpy

from matplotlib import pyplot


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
    x = numpy.array([9, 46, -12, -18, -7, -14, 38, -28 , 40, -37, 29])
    y = numpy.array([-22, -41, 6, 25, -41, 45, -46, 50, 33, -6, 36])

    _x = numpy.linspace(-100, 100, 1000)

    _y = [lagrange(x, y, z) for z in _x]

    Y = 500
    pyplot.ylim((-Y, Y))

    pyplot.scatter(x, y, c='green')
    pyplot.plot(_x, _y, 'red')
    pyplot.show()
