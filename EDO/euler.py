import numpy

from matplotlib import pyplot


def euler(y, f, h):
    r = [y[0]]
    for n, x in enumerate(y[1:]):
        r.append(r[n] + f(r[n]) * h)
    return r


if __name__ == '__main__':
    x_beg = 0.
    x_end = numpy.pi/2.

    n_points = 500

    dx = (x_end - x_beg) / n_points

    x_val = numpy.linspace(x_beg, x_end, n_points)
    y_val = [numpy.sin(x) for x in x_val]

    y_sim = euler(y=y_val, f=lambda x: numpy.sqrt(1-x**2), h=dx)

    pyplot.plot(x_val, y_val, 'r-', label='$y=e^x$')
    pyplot.scatter(x_val, y_sim, c='b', s=2, label='$y\'=y$')
    pyplot.legend()
    pyplot.show()
