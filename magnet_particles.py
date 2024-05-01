import numpy as np
from math import pi, factorial

# 1. Create the force function
# 2. Choose the approach method: Two sumations
    # a. Summation of k values over range of k=1 to k=K
    # b. Summation of n values over range of n=1 to n=N
# 3. Loop over the n range and find summation for a value k
# 4 Sum all the over range of K
def doubles(maxk, maxn=10):
    force = lambda k : sum([(1 / (k*(n+1)**(2*k))) for n in range(1, maxn+1)])
    return sum(list(map(force, range(1, maxk+1))))
# print(doubles(20, 10000))