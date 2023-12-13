from itertools import permutations

def next_bigger(n):
    perms = permutations(str(n))
    perm_numbers = []
    for number in perms:
        no = ''
        for digit in number:
            no += digit
        perm_numbers.append(int(no))
    perm_numbers = sorted(perm_numbers)
    i = perm_numbers.index(n)
    if i == len(perm_numbers):
        return n
    v = perm_numbers[i + 1]
    if v == n:
        return -1
    else:
        return v

print(next_bigger(2017))