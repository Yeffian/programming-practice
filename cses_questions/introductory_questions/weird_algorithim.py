def weird_algorithim(n):
    current = n

    while current != 1:
        print(int(current), end=' ')
        if current % 2 == 0:
            current = current / 2
        else:
            current = current * 3 + 1
    
    print('1')

n = int(input())
weird_algorithim(n) 