def solve(n, m, spotty, clear):
    result = 0
    for j in range(m):
        spotty_chars = {cow[j] for cow in spotty}
        clear_chars = {cow[j] for cow in clear}

        if spotty_chars.isdisjoint(clear_chars):
            result += 1

    return result


with open('cownomics.in', 'r') as file:
    lines = file.readlines()
    n, m = map(int, lines[0].split())
    spotty = [lines[i + 1].strip() for i in range(n)]
    clear = [lines[n + i + 1].strip() for i in range(n)]

ans = solve(n, m, spotty, clear)

with open('cownomics.out', 'w') as file:
    file.write(str(ans) + '\n')
