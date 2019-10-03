import numpy

TOL = .00001


def newton(f, df, x0, D2d):
    g = lambda x: x - (f(x)/df(x))

    r = g(x0)
    while D2d * abs(r - x0)**2 > TOL:
        x0 = r
        r = g(x0)
    return r


if __name__ == '__main__':
    f = lambda x: x - numpy.log(15 - numpy.log(x))
    df = lambda x: 1 + 1 / (x * (15 - numpy.log(x)))

    r = newton(f, df, 1, 9/(3*(numpy.sqrt(3)-1)+numpy.pi))
    print('r = ' + str(r) + ' f(r) = ' + str(f(r)))