def unique_in_order(sequence):
    if not sequence:
        return []

    result = [sequence[0]]

    for item in sequence[1:]:
        if item != result[-1]:
            result.append(item)

    return result