def digital_root(n):
    numbers = list(str(n))
    result = 0

    for num in numbers:
        result += int(num)
    
    if len(str(result)) > 1:
        return digital_root(result)
    else:
        return result

print(digital_root(942))