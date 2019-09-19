import numpy

TOL = 0.001


def regula_falsi(function, a, b):
    x = None

    while abs(b - a) > TOL:
        x = (a*function(b) - b*function(a)) / (function(b) - function(a))
        if function(x) * function(a) > 0:
            a = x
        else:
            b = x

    return x


if __name__ == '__main__':
    print(regula_falsi(lambda x: x**(1/2)*numpy.sin(x) - x**3 + 2, a=1, b=2))