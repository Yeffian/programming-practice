def move_zeros(lst):
    result = []
    zero_count = 0
    for n in lst:
        if n != 0: 
            result.append(n)
        else:
            zero_count += 1
    for i in range(zero_count):
        result.append(0)
    return result