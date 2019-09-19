import numpy

TOL = .00001


def fixed_point(function, x0, k):
    x = function(x0)
    while (k / (1 - k))*abs(x-x0) > TOL:
        x0 = x
        x = function(x0)
    return x


if __name__ == '__main__':
    f = lambda x: x - numpy.log(15 - numpy.log(x))
    g = lambda x: numpy.log(15 - numpy.log(x))

    r = fixed_point(function=g, x0=(1+3)/2, k=1/12)
    print('r = ' + str(r) + ' f(r) = ' + str(f(r)))
