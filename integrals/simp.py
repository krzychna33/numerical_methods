from sympy import *
import numpy as np


x = Symbol('x')
v = x**2 * cos(x)
f = lambdify(x, v, "numpy")

A = 0
B = np.pi

space = B - A
STEPS = 40
H = space/STEPS

acc = f(A) + f(B)

for i in range(1, STEPS, 2):
    print(i)
    acc+=f(i * H + A) * 4

for i in range(2, STEPS-1, 2):

    acc+=f(i * H + A) * 2


acc = H/3 * acc

print(acc)