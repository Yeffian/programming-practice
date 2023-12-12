def lucasnum(n, memo={0:2, 1:1}):
    if n in memo: return memo[n]
    if n < 0:
        memo[n] = lucasnum(n + 2, memo) - lucasnum(n + 1, memo)
    else:
        memo[n] = lucasnum(n - 1, memo) + lucasnum(n - 2, memo)
    return memo[n]