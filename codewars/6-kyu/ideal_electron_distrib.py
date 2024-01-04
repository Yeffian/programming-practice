def atomic_number(electrons):
    shells = []
    shell_no = 1
    temp = 0
    capacity = 2 * shell_no ** 2
    for e in range(1, electrons + 1):
        # Shell_N = 2n^2
        if temp == capacity:
            shells.append(temp)
            shell_no += 1
            capacity = 2 * shell_no ** 2
            temp = 1
        else:
            temp += 1
        
    shells.append(temp)

    return shells

print(atomic_number(11))