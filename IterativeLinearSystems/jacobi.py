import numpy

TOL = .0001


def jacobi(A, b):
    x0 = numpy.zeros_like(b)
    t = numpy.zeros_like(A)
    c = numpy.zeros_like(b)

    for i, line in enumerate(A):
        c[i] = b[i]/A[i][i]
        for j, column in enumerate(line):
            if i != j:
                t[i][j] = -(A[i][j]/A[i][i])

    x = numpy.matmul(t, x0) + c

    t_inf_norm = numpy.linalg.norm(t, numpy.inf)

    p = t_inf_norm / (1 - t_inf_norm)
    while p * numpy.linalg.norm(x - x0, numpy.inf) > TOL:
        x0 = x
        x = numpy.matmul(t, x0) + c
    return x


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

    with open('jacobi_out.txt', 'w') as f:
        for s in linear:
            print('\n--- Solving Linear System Ax=b (JACOBI) ---', file=f)
            print('A=', file=f), print(s['A'], file=f)
            print('b=', file=f), print(s['b'], file=f)
            print('x=', file=f), print(jacobi(A=s['A'], b=s['b']), file=f)
