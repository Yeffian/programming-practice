def count_primes_less_than(n: int) -> int:
    # Sieve of Eratosthenes
    results = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            results.append(i)

    return len(results)