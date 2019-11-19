import numpy

from matplotlib import pyplot


def F(x):
    if len(x) == 1:
        return x[0][1]
    else:
        return (F(x[1:]) - F(x[:-1])) / (x[len(x)-1][0] - x[0][0])


class NewtonPolynomial:
    def __init__(self, p):
        self.c = [0]
        self.p = p
        self.n = 0

    def init(self):
        for _ in range(len(self.p)):
            x = self.p[0:self.n + 1]
            if self.n == 0:
                self.c[self.n] = F(x)
            else:
                self.c[self.n] = (F(x[1:]) - self.c[self.n - 1]) / (x[len(x) - 1][0] - x[0][0])
            self.n = self.n + 1
            self.c.append(0)
        self.c.pop()

    def update(self, point):
        self.c.append(0)
        self.p.append(point)

        x = self.p[0:self.n + 1]

        self.c[self.n] = (F(x[1:]) - self.c[self.n - 1]) / (x[len(x)-1][0] - x[0][0])
        self.n = self.n + 1

    def evaluate(self, x):
        value = 0.
        x_values = [p[0] for p in self.p]
        for n, c in enumerate(self.c):
            prod = c
            for i in range(n):
                prod = prod * (x - x_values[i])
            value = value + prod
        return value


if __name__ == '__main__':
    fig, axs = pyplot.subplots(3)

    fig.suptitle('Interpolação Polinomial - Diferenças Divididas')

    X = numpy.linspace(-10, 10., 100)

    p = lambda x: 9*x**3 + 3*x**2 - 12*x - 12

    l2_zero = 1 / numpy.sqrt(3)

    points = [(l2_zero, p(l2_zero)), (-l2_zero, p(-l2_zero))]

    np = NewtonPolynomial(p=points)

    np.init()

    print(np.c)

    Y = [np.evaluate(x_i) for x_i in X]
    axs[0].plot(X, Y, 'r-')
    axs[0].scatter([p[0] for p in points], [p[1] for p in points], c='blue')

    np.update((4, 10))
    Y = [np.evaluate(x_i) for x_i in X]
    axs[1].plot(X, Y, 'r-')
    axs[1].scatter([p[0] for p in points], [p[1] for p in points], c='blue')

    print(np.c)

    np.update((-8, -12))
    Y = [np.evaluate(x_i) for x_i in X]
    axs[2].plot(X, Y, 'r-')
    axs[2].scatter([p[0] for p in points], [p[1] for p in points], c='blue')

    pyplot.show()


