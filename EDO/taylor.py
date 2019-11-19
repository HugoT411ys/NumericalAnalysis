import numpy

from matplotlib import pyplot


def fh(t=None, u=None): return t**2*u + u*(1-u)


def fh2(t=None, u=None): return 2*t*u + t**2*(1-2*u)*(t**2*u+u*(1-u))


def taylor(u_t1, t1, t2, h):
    t = numpy.arange(t1, t2, h)
    u = numpy.zeros_like(t)
    u[0] = u_t1
    for n, _ in enumerate(u[:-1]):
        u[n+1] = u[n] + h * fh(t=t[n], u=u[n]) * 0.5*h**2 * fh2(t=t[n], u=u[n])
    return u


if __name__ == '__main__':
    h = 1/500
    a, b = 0., 5.

    t_val = numpy.arange(a, b, h)
    u_val = taylor(u_t1=1, t1=a, t2=b, h=h)

    # pyplot.plot(t_val, (1/999) * numpy.exp(t_val * (-1/10)) + (4994/999) * numpy.exp(-100*t_val), 'r')
    pyplot.scatter(t_val, u_val, c='b', s=2)

    pyplot.show()
