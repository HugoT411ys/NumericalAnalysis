import numpy


def comp_simpson(a, b, func, error, step):
    n = (b - a) / step
    s = 0.
    for i in range(int(n)):
        s = simpson(a+i*step, a+(i+1)*step, func) + s
    return s


def simpson(a, b, func):
    h = 0.5 * (b + a)
    return (1/3) * h * (func(a) + func(b) + 4 * func(h))


def main():
    print(simpson(a=0., b=1., func=lambda x: 4*x**3))
    print(comp_simpson(a=0., b=1., func=lambda x: 4*x**3, step=.1, error=0.))


if __name__ == '__main__':
    main()
