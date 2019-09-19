import numpy

TOL = .0001


def gauss_seidel(A, b):
    x0 = numpy.zeros_like(b)

    while True:
        x = numpy.zeros_like(x0)
        for i in range(A.shape[0]):
            sum = 0
            for j in range(i):
                sum += A[i][j] * x[j]
            for j in range(i+1, A.shape[0]):
                sum += A[i][j] * x0[j]
            x[i] = (b[i] - sum) / A[i][i]

        if numpy.linalg.norm(x-x0, numpy.inf) < TOL:
            return x

        x0 = x


if __name__ == '__main__':
    # Solving A * x = b

    linear = [
        {
            'A': numpy.array([[10., 1.], [1., 8.]]),
            'b': numpy.array([23., 26.])
        },
        {
            'A': numpy.array([[2., 1., 0.], [1., -3., 0.], [0., 1., 3.]]),
            'b': numpy.array([-1., 0., 0.])
        },
        {
            'A': numpy.array([[9., 5., -1.], [3., 8., -3.], [1., 1., 4.]]),
            'b': numpy.array([2., 9., 11.])
        },
        {
            'A': numpy.array([[7., -5., 1.], [3., 10., -2.], [-2., 3., 4.]]),
            'b': numpy.array([7., 8., 9.])
        }
    ]

    with open('gauss_out.txt', 'w') as f:
        for s in linear:
            print('\n--- Solving Linear System Ax=b (GAUSS-SEIDEL) ---', file=f)
            print('A=', file=f), print(s['A'], file=f)
            print('b=', file=f), print(s['b'], file=f)
            print('x=', file=f), print(gauss_seidel(A=s['A'], b=s['b']), file=f)
