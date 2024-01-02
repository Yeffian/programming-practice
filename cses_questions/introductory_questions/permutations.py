def permutations(n):
    if n == 2:
        print('NO SOLUTION')
        return
    
    if n == 3:
        print('NO SOLUTION')
        return
    
    # i dont like doing this but idk how to fix it
    if n == 4:
        print('2 4 1 3')
        return
    
    permutations = []

    for i in range(1, n + 1, 2):
        permutations.append(str(i))

    for i in range(2, n + 1, 2):
        permutations.append(str(i))
    
    print(' '.join(permutations))

permutations(int(input()))