import numpy

TOL = 1/30


def bisection(function, a, b):
    if function(a)*function(b) > 0:
        return 'Invalid interval'

    x = None

    while abs(b - a) > TOL:
        x = (a + b) / 2
        if function(x)*function(a) > 0:
            a = x
        else:
            b = x

    return x


if __name__ == '__main__':
    f = lambda x: x**(1/2)*numpy.sin(x) - x**3 + 2
    print(bisection(function=f, a=1, b=2))