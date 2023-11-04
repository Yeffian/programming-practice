import math

def is_perfect_square(number):
    root = int(math.sqrt(number))

    return ((root * root) == number)

def count_perfect_square(numbers):
    squares = 0
    numbers = [int(n) for n in numbers.split(' ')]

    for number in numbers:
        if is_perfect_square(number):
            squares += 1
    
    return squares

with open('squares_q6.txt', "r") as file:
    print(count_perfect_square(file.read()))

