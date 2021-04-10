import numpy as np
A = np.array([[1,1,1,1], [0,1,2,3], [0,0,2,6], [0,0,0,6]])
B = [2,5,8,12]

X = np.linalg.inv(A).dot(B)

print(X)
