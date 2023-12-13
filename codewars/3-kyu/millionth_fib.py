import numpy as np

def fib(n):
    mat = np.matrix([[1, 1], [1, 0]], dtype=object) ** abs(n)
    if n % 2 == 0 and n < 0:
        return -mat[0, 1]
    
    return mat[0, 1]