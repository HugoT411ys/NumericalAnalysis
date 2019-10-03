import numpy

TOL = .00001


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


def get_coefficients(n):
    A = numpy.zeros((n, n))

    for i in range(n):
        if 0 < i < 10:
            A[i][i-1] = A[i][i+1] = -1
            A[i][i] = 5

    A[0][0] = 1
    A[0][1] = -1

    A[10][9] = -1
    A[10][10] = 2

    return A


if __name__ == '__main__':
    # Solving A * x = b

    linear = {
        'A': get_coefficients(11),
        'b': numpy.array([numpy.cos((i+1)/10) for i in range(11)])
    }

    # adjusting the b vector
    linear['b'][0] = linear['b'][10] = 0

    print(linear['A'], linear['b'])

    with open('problema7_out.txt', 'w') as f:
        print('\n--- Solving Linear System Ax=b (JACOBI) ---', file=f)
        print('A=', file=f), print(linear['A'], file=f)
        print('b=', file=f), print(linear['b'], file=f)
        print('x=', file=f), print(jacobi(A=linear['A'], b=linear['b']), file=f)
