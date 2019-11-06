from Polynomial_Interpolation.lagrange import *


def f(x):
    return 1./(1. + 16.*(x**2))


if __name__ == '__main__':
    iterations = [10, 20, 40]

    fig, axs = pyplot.subplots(3)
    # fig.suptitle('Pontos Igualmente Espaçados')

    fig.suptitle('Pontos de Chebyshev')

    axs[0].set_ylim(-0.5, 1.5)
    axs[1].set_ylim(-0.5, 1.5)
    axs[2].set_ylim(-0.5, 1.5)

    for j, n in enumerate(iterations):
        X = numpy.linspace(-1., 1., 1000)

        '''x_eq = [-1. + 2*(i-1)/(n-1) for i in range(1, n+1)]
        y_eq = [f(x_i) for x_i in x_eq]'''

        x_ch = [numpy.cos(((2*i-1.)*numpy.pi)/(2*n)) for i in range(1, n+1)]
        y_ch = [f(x_i) for x_i in x_ch]

        '''axs[j].plot(X, [lagrange(x_eq, y_eq, x) for x in X], 'r-')
        axs[j].scatter(x_eq, y_eq, c='blue', s=10)'''

        axs[j].plot(X, [lagrange(x_ch, y_ch, x) for x in X], 'r-')
        axs[j].scatter(x_ch, y_ch, c='blue', s=10)

    pyplot.show()
