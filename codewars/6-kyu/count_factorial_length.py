from math import log10, floor, pi, e

def count(n):
    stirling = (n * log10(n / e) + log10(2 * pi * n) / 2.0)
    return floor(stirling) + 1