def solve(n, t):
    pos = 0
    # true means left to right
    # false means right to left
    dir = True

    for ct in range(0, t):
        print(ct, dir, pos)

        if pos == n:
            pos = 0
            dir = not dir
        else:
            if dir is True:
                pos += 1
            else:
                pos -= 1

        # print('time', ct, 'pos', pos)

    return pos

print(solve(7, 17))