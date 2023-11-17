def move_zeros(lst):
    zeros = 0
    non_zero = []

    for i in lst:
        if i == 0:
            zeros += 1
        else:
            non_zero.append(i)
    
    for i in range(zeros):
        non_zero.append(0)
    
    return non_zero

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))