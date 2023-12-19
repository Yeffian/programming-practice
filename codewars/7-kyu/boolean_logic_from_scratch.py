def func_or(a,b):
    a = bool(a)
    b = bool(b)
    if a is True and b is False:
        return True
    if a is False and b is True:
        return True
    if a is True and b is True:
        return True
    else:
        return False


def func_xor(a,b):
    a = bool(a)
    b = bool(b)
    if a is True and b is True:
        return False
    else:
        return func_or(a,b)