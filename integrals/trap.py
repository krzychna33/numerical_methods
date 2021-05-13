import numpy as np

def f(x):
    return np.power(x, 2) * np.cos(x)

A = 0
B = np.pi

space = B - A
steps = 40
H = space/steps

acc = f(A) + f(B)
for i in range(1, steps):
    print(i)
    acc += 2* f(i*H + A)

val = 0.5 * H * acc
print(val)