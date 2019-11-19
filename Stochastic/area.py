import numpy


def monte_carlo(a, b, n):
    s = 0
    points = numpy.random.uniform(0., a, (n, 2))
    for p in points:
        x, y = p[0], p[1]
        if (x/a)**2 + (y/b)**2 <= 1:
            s = s + 1
    return 4*(a**2)*(s/n)


def main():
    n = 1000000
    a, b = 3, 2

    print('Exact Area = ' + str(numpy.pi * a * b))
    print('Estimated Area = ' + str(monte_carlo(a, b, n)))


if __name__ == '__main__':
    main()
