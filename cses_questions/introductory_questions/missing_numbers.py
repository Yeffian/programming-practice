def missing_numbers(n, l):
    input_set = set(l)
    true_set = set(list(range(1, n + 1)))

    print(true_set.difference(input_set).pop())

n = int(input())
l = [int(num) for num in input().split()]
missing_numbers(n, l)