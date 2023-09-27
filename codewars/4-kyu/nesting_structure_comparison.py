test1 = [ 1, [1, 2, 3], [1, 2, [3, 4] ]]
test2 = [ 4, [7, 6, 2], [9, 8, [6, 0] ], [1, 2]]

def replace_array_values(A, n):
    result = []
    for v in A:
        if hasattr(v, "__len__"):
            result.append(replace_array_values(v, n))
        else:
            result.append(n)
    return result

    
def same_structure_as(original,other):
    original_buff = replace_array_values(original, 0)
    other_buff = replace_array_values(other, 0)

    return original_buff == other_buff

print(same_structure_as(test1, test2))