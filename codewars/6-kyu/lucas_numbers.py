def lucasnum(n, memo={0:2, 1:1}):
    if n in memo: return memo[n]
    if n < 0:
        memo[n] = lucasnum(n + 2) - lucasnum(n + 1)
    else:
        memo[n] = lucasnum(n - 1) + lucasnum(n - 2)
    return memo[n]