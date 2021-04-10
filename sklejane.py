import numpy as np
from sympy import Symbol, simplify, lambdify, Rational, Poly, diff

import matplotlib.pyplot as plt

def get_cmap(n, name='hsv'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')

def sklej(X, Y):
    n = len(X)
    h = [0 for _ in range(n)]
    b = [0 for _ in range(n)]
    u = [0 for _ in range(n)]
    v = [0 for _ in range(n)]
    z = [0 for _ in range(n)]
    for i in range(n - 1):
        print(i)
        h[i] = X[i + 1] - X[i]
        b[i] = 6 * (Y[i + 1] - Y[i]) / h[i]

    u[1] = 2 * (h[0] + h[1])
    v[1] = b[1] - b[0]

    for i in range(2, n - 1):
        print(i)
        u[i] = 2 * (h[i] + h[i - 1]) - np.power(h[i - 1], 2) / u[i - 1]
        v[i] = (b[i] - b[i - 1]) - h[i - 1] * v[i - 1] / u[i - 1]

    for i in range(n - 2, 0, -1):
        print(i)
        z[i] = (v[i] - h[i] * z[i + 1]) / u[i]

    x = Symbol('x')
    S = []
    for i in range(n - 1):
        B = -1 * h[i] / 6 * z[i + 1] - h[i] / 3 * z[i] + 1 / h[i] * (Y[i + 1] - Y[i])
        temp = Y[i] + (x - X[i])*(B + (x - X[i])*(z[i]/2 + 1/6*h[i]*(x-X[i])*(z[i+1] - z[i])))
        S.append(simplify(temp))


    lambdas = []
    cmap = get_cmap(len(S))
    for i in range(n-1):
        print(S[i])
        poly = Poly(S[i], x)
        print(poly.coeffs())
        lm = lambdify(x, S[i], "numpy")
        lambdas.append(lm)

    return lambdas

def calculate_skl(X, L, x):
    n= len(L)
    cmap = get_cmap(n)

    a = int(np.floor(x))
    val = L[a](x)
    print("f({}) = {}".format(x, val) )
    for i in range(n-1):
        space = np.arange(X[i],X[i+1], 0.01)
        plt.plot(space, L[i](space), c=cmap(i))

    plt.show()





X = [0, 1, 2, 3, 4]
Y = [0, 0, 0, 1, 0]
Ls = sklej(X, Y)
calculate_skl(X, Ls, 2.25)