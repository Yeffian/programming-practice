import math


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2


def list_squared(m, n):
    results = []
    for i in range(m, n):
        ds = list(divisorGenerator(i))
        for j in range(len(ds)):
            ds[j] = ds[j] ** 2
        s = sum(ds)
        if is_square(s):
            results.append([int(i), int(s)])
    return results


print(list_squared(1, 250))