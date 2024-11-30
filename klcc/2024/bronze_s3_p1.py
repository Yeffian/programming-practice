def solve(n):
    if n % 2 == 0:
        return int((n + 4) / 2 + 0.25 * n ** 2)
    else:
        return int((n + 3) / 2 + n ** 2)

print(solve(500))
print(solve(999))
print(solve(10101))