"""
Computing prime numbers with the archimedean sieve.

(Of course, this is not an optimal way for computing prime numbers...)

"""


import numpy as np

eratosthenes = True

# maximum number
N = 10000

# mask for prime numbers
mask = np.ones([N], dtype=bool)

# simple prime sieve
mask[:2] = False
for j in range(2, int(np.sqrt(N)) + 1):
    if eratosthenes and mask[j] or not eratosthenes:
        mask[j*j::j] = False

# print indices where mask is True
print(np.nonzero(mask)[0])
