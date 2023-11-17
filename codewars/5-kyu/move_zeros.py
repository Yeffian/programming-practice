def move_zeros(lst):
    zeros = 0
    result = []

    for i in lst:
        if i == 0:
            zeros += 1
        else:
            result.append(i)
    
    for i in range(zeros):
        result.append(0)
    
    return result

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))