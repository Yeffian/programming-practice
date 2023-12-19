def is_prime(n):
    if n <= 1: return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def find_primes(n):
    p = []
    for i in range(2, n + 1):
        if is_prime(i):
            p.append(i)
    return p

def summation_of_primes(primes):
    return sum(find_primes(primes))