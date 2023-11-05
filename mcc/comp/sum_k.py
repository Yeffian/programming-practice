from itertools import chain, combinations
from numba import jit
import json

@jit
def custom_sum(s):
    result = 0

    for i in s:
        result += i
    
    return result

@jit
def powerset(s):
    x = len(s)
    masks = [1 << i for i in range(x)]
    for i in range(1, 1 << x):
        yield [ss for mask, ss in zip(masks, s) if i & mask]

@jit
def sum_k(k, a):
    result = 0

    for s in powerset(a):
        score = sum(s) ** k
        result += score
    
    return result % 998244353


with open(r"C:\Users\aditc\dev\competitive-programming-practise\mcc\comp\sum_k_questions.json", "r") as file:
    questions = json.loads(file.read())

    task = "task4"

    a = [int(a) for a in questions[task]['A'].split(' ')]
    k = questions[task]['k']
    print(sum_k(k, a))
        