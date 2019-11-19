import numpy

from matplotlib import pyplot


def function(t, u): return t**2 * u + u * (1 - u)


def taylor_second(u_t1, t1, t2, h, f):
    t = numpy.arange(t1, t2, h)
    u = numpy.zeros_like(t)
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        temp = f(t[n], u[n])
        u[n + 1] = u[n] + h * temp + 0.5*h**2 * (2*t[n]*u[n] + ((t[n]**2 + 1 - 2*u[n])*temp))
    return u


def taylor_third(u_t1, t1, t2, h, f):
    t = numpy.arange(t1, t2, h)
    u = numpy.zeros_like(t)
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        temp = f(t[n], u[n])
        u[n + 1] = u[n] + h * temp + 0.5*h**2 * (2*t[n]*u[n] + ((t[n]**2 + 1 - 2*u[n])*temp))
    return u


def euler(u_t1, t1, t2, h, f):
    t = numpy.arange(t1, t2, h)
    u = numpy.zeros_like(t)
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        u[n+1] = u[n] + h * f(t[n], u[n])
    return u


def runge_kutta(u_t1, t1, t2, h, f):
    t = numpy.arange(t1, t2, h)
    u = numpy.zeros_like(t)
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        k1 = h * f(t[n], u[n])
        k2 = h * f(t[n] + 0.5*h, u[n] + 0.5*k1)
        k3 = h * f(t[n] + 0.5*h, u[n] + 0.5*k2)
        k4 = h * f(t[n] + h, u[n] + k3)

        u[n+1] = u[n] + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    return u


if __name__ == '__main__':
    h = 1/10
    a, b = 0., 5.

    t_val = numpy.arange(a, b, h)

    u_val = runge_kutta(u_t1=1, t1=a, t2=b, h=h, f=function)
    pyplot.scatter(t_val, u_val, c='b')

    u_val = euler(u_t1=1, t1=a, t2=b, h=h, f=function)
    pyplot.scatter(t_val, u_val, c='r')

    u_val = taylor_second(u_t1=1, t1=a, t2=b, h=h, f=function)
    pyplot.scatter(t_val, u_val, c='g')

    pyplot.show()