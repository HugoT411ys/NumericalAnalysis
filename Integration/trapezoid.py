import numpy


def comp_trapezoid(a, b, func, error, step):
    n = (b - a) / step
    s = 0.5 * step * (func(a) + func(b))
    p = 0.
    for i in range(1, int(n)):
        p = p + func(a + i*step)
    return s + step * p


def trapezoid(a, b, func):
    h = b - a
    return 0.5*h * (func(a) + func(b))


def main():
    print(trapezoid(a=0., b=1., func=lambda x: x**2))
    print(comp_trapezoid(a=0., b=1., func=lambda x: x**2, error=0.001, step=.001))


if __name__ == '__main__':
    main()
