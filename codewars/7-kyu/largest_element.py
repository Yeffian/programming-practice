def largest(n, xs):
    arr = sorted(xs, reverse=True)
    return sorted(arr[:n])

print(largest(2, [7,6,5,4,3,2,1]))