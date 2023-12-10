import functools

# it was too slow
@functools.lru_cache(maxsize=None)
def kelleher_sullivan_partitions(n):
    a = [1] * n
    y = -1
    v = n
    while v > 0:
        v -= 1
        x = a[v] + 1
        while y >= 2 * x:
            a[v] = x
            y -= x
            v += 1
        w = v + 1
        while x <= y:
            a[v] = x
            a[w] = y
            yield a[:w + 1]
            x += 1
            y -= 1
        a[v] = x + y
        y = a[v] - 1
        yield a[:w]

def partitions(n):
    p = kelleher_sullivan_partitions(n)
    return len(list(p))

print(partitions(5))