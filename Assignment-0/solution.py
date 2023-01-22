import numpy as np


alpha = 3
delta = -2
lam = 0.5
N = 10000
np.random.seed(0)

A = np.zeros(shape=(N, 3))
b = np.zeros(shape=(N, 1))

for i in range(N):

    x1 = np.random.normal(0,1)


    epsilon = np.random.uniform(-1, 1)
    x2 = alpha + (.2 * x1) + epsilon

    y = delta + (1.2 * x1) + np.random.exponential(lam)

    A[i] = [delta, x1, x2]
    b[i] = [y]

x = np.linalg.lstsq(b, A)

print(f"{A}\n\n{b}\n\n{x}")
