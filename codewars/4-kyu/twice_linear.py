from bisect import bisect

def my_insort(a, x):
    if x > a[-1]:
        a.append(x)
        return
    ip = bisect(a, x)
    if x != a[ip-1]:
        a.insert(ip, x)

def dbl_linear(n):
    u_list= [1]
    for i in range(0, n+1):
        my_insort(u_list, u_list[i] * 2 + 1)
        my_insort(u_list, u_list[i] * 3 + 1)
    return u_list[n]
