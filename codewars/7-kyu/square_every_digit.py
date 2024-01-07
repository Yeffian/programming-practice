def square_digits(num):
    result = ""
    for n in str(num):
        result += str(int(n) ** 2)
    return int(result)