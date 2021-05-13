from newton import newton_interpolation1_raw
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def get_chybyshev_nodes(a, b, n):
    nodes = []
    for i in range(n):
        temp = 0.5 * ((b - a) * np.cos(((2 * i + 1) / (2 * n + 2)) * np.pi) + a + b)
        nodes.append(temp)
    return nodes


def r(x):
    return 1 / (1 + np.power(x, 2))


if __name__ == "__main__":
    X = [x for x in range(-5, 6, 1)]
    Y = [r(x) for x in X]
    print(X)
    print(Y)


    k = np.arange(-5, 5, 0.1)
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')


    # Xch = get_chybyshev_nodes(-5, 5, 5)
    # Ych = [1 / (1 + np.power(x, 2)) for x in Xch]
    # plt.plot(k, newton_interpolation1_raw(Xch, Ych)(k), 'r')

    Xch = get_chybyshev_nodes(-5, 5, 9)
    Ych = [1 / (1 + np.power(x, 2)) for x in Xch]
    plt.plot(k, newton_interpolation1_raw(Xch, Ych)(k), 'g')

    # Xch = get_chybyshev_nodes(-5, 5, 15)
    # Ych = [1 / (1 + np.power(x, 2)) for x in Xch]
    # plt.plot(k, newton_interpolation1_raw(Xch, Ych)(k), 'b')

    plt.plot(k, newton_interpolation1_raw(X, Y)(k), 'y')

    plt.plot(k, r(k), 'm')
    plt.show()
