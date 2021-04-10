from sympy import Symbol, simplify, lambdify, Rational, Poly, diff
import numpy as np
import matplotlib.pyplot as plt


def pd(X, Y):
    if len(Y) == 1:
        return Y[0]
    return Rational((pd(X[:len(X) - 1], Y[:len(Y) - 1]) - pd(X[1:], Y[1:])), (X[0] - X[len(X) - 1]))


def pd2(X, Y):
    if len(Y) == 1:
        return Y[0]
    return (pd(X[:len(X) - 1], Y[:len(Y) - 1]) - pd(X[1:], Y[1:])) / (X[0] - X[len(X) - 1])


def newton_interpolation1_raw(X, Y):
    print('--- NEWTON INTERPOLATION ---')

    x = Symbol('x')
    accumulator = 0
    for i in range(len(X)):
        pdv = pd(X[:i + 1], Y[:i + 1])
        if i == 0:
            accumulator += pdv
        else:
            m = 1
            for j in range(i):
                m *= (x - X[j])
            accumulator += pdv * m
    print(accumulator)
    print(simplify(accumulator))
    poly = Poly(accumulator, x)
    print(poly.coeffs())
    return lambdify(x, accumulator, "numpy")

def newton_interpolation1(X, Y, v):
    print('--- NEWTON INTERPOLATION ---')

    x = Symbol('x')
    accumulator = 0
    for i in range(len(X)):
        pdv = pd(X[:i + 1], Y[:i + 1])
        if i == 0:
            accumulator += pdv
        else:
            m = 1
            for j in range(i):
                m *= (x - X[j])
            accumulator += pdv * m
    print(accumulator)
    print(simplify(accumulator))
    poly = Poly(accumulator, x)
    print(poly.coeffs())

    return lambdify(x, accumulator, "numpy")(v)


def newton_interpolation2(X, Y, v):
    x = Symbol('x')
    accumulator = Poly(0, x)
    for i in range(len(X)):
        pdv = pd(X[:i + 1], Y[:i + 1])
        if i == 0:
            accumulator += pdv
        else:
            m = 1
            for j in range(i):
                m *= (x - X[j])
            accumulator += pdv * m
    print(accumulator)
    print(accumulator.coeffs())

    return accumulator(v)



if __name__ == "__main__":
    # X = [0, 2, 3, 4, 6]
    # Y = [1, 3, 2, 5, 7]

    # X2 = [1, 2, 3, 4]
    # Y2 = [5, 8, 2, 9]

    # X2 = [100, 121, 144]
    # Y2 = [10,11,12]

    # X2 = [-1, 0, 1, 2, 3]
    # Y2 = [-7, -1, -1, -1, 5]

    X2 = [1,2,3,4,5]
    Y2 = [1,5, 14, 30, 55]

    print(newton_interpolation1(X2, Y2, 9))

    k = np.arange(-15, 15, 0.0001)
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(k, newton_interpolation1_raw(X2, Y2)(k), 'r')
    # plt.scatter([np.power(x,2) for x in range(1,12)], [x for x in range(1,12)])

    plt.show()
