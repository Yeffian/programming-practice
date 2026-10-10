t=int(input())
for _ in range(t):
    r,c=map(int, input().split())

    # on the diagonal
    if r==c:
        print((r*r)-(r-1))

    # if on top of diagonal
    if c>r:
        diag=(c*c)-(c-1)
        offset=abs(c-r)
        if c%2==0:
            print(diag-offset)
        else:
            print(diag+offset)
    # if below the diagonal
    if c<r:
        diag=(r*r)-(r-1)
        # even numbered rows
        if r%2==0:
            offset=abs(c-r)
            print(diag+offset)
        else:
            offset=abs(c-r)
            print(diag-offset)


