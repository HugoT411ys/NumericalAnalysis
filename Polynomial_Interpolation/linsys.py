import numpy

from matplotlib import pyplot


def main():
    x = numpy.array([
        [1., -1., 1, -1.],
        [1, .5, .5**2, .5**3],
        [1., 1., 1., 1.],
        [1, 1.25, 1.25**2, 1.25**3]
    ])

    y = numpy.array([1.25, 0.5, 1.25, 1.8125])

    inv_x = numpy.linalg.inv(x)

    a = inv_x.dot(y)

    print(a)

    _x = [-1., .5, 1., 1.25]
    _y = [1.25, .5, 1.25, 1.8125]

    x_ = numpy.linspace(-2., 2., 100)
    y_ = [a[0] + x*a[1] + x**2 * a[2] + x**3 * a[3] for x in x_]

    pyplot.scatter(_x, _y)
    pyplot.plot(x_, y_)
    pyplot.show()


if __name__ == '__main__':
    main()
