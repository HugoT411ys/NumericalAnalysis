import numpy

from matplotlib import pyplot


def f_2(t=None, u=None): return -(1/10) * u


def f_1(t=None, u=None): return -100*u


def f(t=None, u=None): return -10*u


def heun(u_t1, t1, t2, h, function):
    u = numpy.zeros_like(numpy.arange(t1, t2, h))
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        u[n+1] = u[n] + 0.5*h * (function(u=u[n]) + function(u=u[n] + h * function(u=u[n])))
    return u


def forward_euler(u_t1, t1, t2, h, function):
    u = numpy.zeros_like(numpy.arange(t1, t2, h))
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        u[n+1] = u[n] + h * function(u=u[n])
    return u


def double_forward_euler(u_t1, t1, t2, h, function1, function2):
    u = numpy.zeros_like(numpy.arange(t1, t2, h))
    u[0] = u_t1
    v = forward_euler(u_t1=1., t1=t1, t2=t2, h=h, function=function2)
    for n, _ in enumerate(u[:-1]):
        u[n+1] = u[n] + h * (function1(u=u[n]) + v[n])
    return u


if __name__ == '__main__':
    h = 1/100
    a, b = 0., 1.

    t_val = numpy.arange(a, b, h)
    u_val = heun(u_t1=1, t1=a, t2=b, h=h, function=f)

    # pyplot.plot(t_val, (1/999) * numpy.exp(t_val * (-1/10)) + (4994/999) * numpy.exp(-100*t_val), 'r')
    pyplot.scatter(t_val, u_val, c='b', s=2)

    pyplot.show()
