import math


def is_square(x):
    root = int(math.sqrt(x))
    return root * root == x


def sum_of_squares(n):
    if is_square(n):
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - (i * i)):
            return 2

    while n % 4 == 0:
        n >>= 2

    if n % 8 == 7:
        return 4

    return 3