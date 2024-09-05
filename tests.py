import timeit

def prefix_sum(n):
    p_sum = [0] * len(n)
    p_sum[0] = n[0]

    for i in range(1, len(n)):
        p_sum[i] = p_sum[i - 1] + n[i]

    return p_sum


def query_from_l_to_r_prefix_sum(n, l, r):
    p_sum = prefix_sum(n)

    return p_sum[r] - p_sum[l - 1]


def query_from_l_to_r(n, l, r):
    sum = 0

    for i in n[l:r+1]:
        sum += i

    return sum


"""
Just to see how much more efficient it really is and if it's actually worth implementing

spoiler alert: it is
"""

start_time = timeit.default_timer()
print(query_from_l_to_r_prefix_sum([8, 3, -2, 4, 10, -1, 0, 5, 3], 2, 7))
print(timeit.default_timer() - start_time)

start_time = timeit.default_timer()
print(query_from_l_to_r([8, 3, -2, 4, 10, -1, 0, 5, 3], 2, 7))
print(timeit.default_timer() - start_time)