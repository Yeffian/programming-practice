def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def solve(start, end):
    nums = []
    for n in range(start, end + 1):
        x = getSum(n)
        if n % x == 0:
            nums.append(n)

    # print(nums)
    return sum(nums)

print(solve(10, 51))
print(solve(100, 2810))