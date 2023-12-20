def solution(array_a, array_b):
    diffs = []
    for i in range(len(array_a)):
        a = array_a[i]
        b = array_b[i]
        
        diff = (a - b) ** 2
        diffs.append(diff)
    return sum(diffs) / len(array_a)