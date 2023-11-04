def calculate_sum(numbers):
    return sum([int(n) for n in numbers.split(' ')])

with open('sums_q6.txt', 'r') as file:
    print(calculate_sum(file.read()))