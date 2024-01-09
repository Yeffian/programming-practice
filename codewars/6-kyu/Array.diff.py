def array_diff(a, b):
    result = []
    for n in a:
        if n not in b:
            result.append(n)
    return result