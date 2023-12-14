from itertools import permutations as perms

def permutations(s):
    p = perms(s)
    results = []
    for item in p:
        results.append(''.join(item))
    return list(set(results))