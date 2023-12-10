import math

#https://www.codewars.com/kata/55b22ef242ad87345c0000b2/train/python
def choose(n, k):
    return math.comb(n, k)


print(choose(100,10))