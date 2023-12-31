import functools

@functools.lru_cache(maxsize=None)
def nth_fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fib(n - 1) + nth_fib(n - 2)
    
print(nth_fib(10))