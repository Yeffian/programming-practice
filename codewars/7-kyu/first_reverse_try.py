def first_reverse_try(arr):
    if len(arr) == 0: return []
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
