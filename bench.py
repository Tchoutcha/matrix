import numpy as np
from time import time

def randomMult():
    x = np.random.randint(0, int(1e10), (3000, 3000))
    y = np.random.randint(0, int(1e10), (3000, 3000))
    return x @ y

def matInv():
    x = np.random.randint(0, int(1e10), (3000, 3000))
    return np.linalg.inv(x)

for i in range(1, 51):
    print(i)

    t = time()
    _ = matInv()
    delta = time() - t
    print('Inversion: %0.2fs' % delta)

    t = time()
    _ = randomMult()
    delta = time() - t
    print('Multiplication: %0.2fs' % delta)
