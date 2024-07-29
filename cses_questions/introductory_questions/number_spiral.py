def number_spiral(x, y):
    m = max(x, y)
    square = (m - 1) * (m - 1)

    if m % 2 == 0:
        if x > y:
            return square + y
        else:
            return (m * m) - x + 1
    else:
        if x > y:
            return (m * m) - y + 1
        else:
            return square + x


print(number_spiral(4, 2))