def solve(s):
    occurences = dict()
    distinct = list(set(s.split(" ")))

    for w in s.split(" "):
        if w in occurences.keys():
            occurences[w] += 1
        else:
            occurences[w] = 1


    return max(occurences.values()) / (len(distinct) - 1), 3



print(solve(open('dracula.txt').read().strip()))
print(solve(open('Drifblim.txt').read().strip()))