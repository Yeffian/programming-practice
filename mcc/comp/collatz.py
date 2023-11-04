import json

def collatz_once(n):
    result = []
    
    for a in n:
        if a % 2 == 0:
            result.append(a / 2)
        else:
            result.append(3 * a + 1)

    return result

def collatz(n, k):
    result = n

    for i in range(k):
        result = collatz_once(result)
        # print(result)
    
    return int(sum(result))


with open("collatz_questions.json", "r") as file:
    questions = json.loads(file.read())

    for task in questions:
        print(f'====== {task} =====')
        n = [int(a) for a in questions[task]['n'].split(' ')]
        k = questions[task]['k']
        print(collatz(n, k))


# print(collatz([3, 1, 4, 1, 5, 9], 3))