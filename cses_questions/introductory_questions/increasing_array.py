def increasing_array(n, x):
    moves = 0
    for i in range(1, len(x)):
        if x[i] < x[i - 1]:
            moves += abs(x[i - 1] - x[i])
            x[i] += abs(x[i - 1] - x[i])

    return moves

n = int(input())
x = [int(num) for num in input().split()]
print(increasing_array(n, x))