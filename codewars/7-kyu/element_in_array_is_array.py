def arr_check(arr):
    for elem in arr:
        if type(elem) is not type([]):
            return False
    
    return True