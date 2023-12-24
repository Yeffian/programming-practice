def missing_numbers(n, l):
    full_range = list(range(1, n + 1))
    sorted_list = list(sorted(l))

    for num in full_range:
        if num not in sorted_list:
            print(num)

n = int(input())
l = [int(num) for num in input().split()]
missing_numbers(n,l)