from sympy import *
from bisection import bisection
from newton_e import newton
from sieczne import sieczne
import numpy as np

x = Symbol("x")
p = -3
q = 3
f_raw = x ** 3 - 5 * x + 3
f = lambdify(x, f_raw, "numpy")

E = np.float_power(10, -3)

p1 = -3
q1 = 3
for i in range(4):
    print('++++')
    p = bisection(f, E, p, q, 100)
    print('--')
    p1 = sieczne(f_raw, E, p1, q1)

