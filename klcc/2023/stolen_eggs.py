n = 5
m = 3
eggs = [1, 2, 4]


original_eggs = list(range(1, n+1))

print(original_eggs)
print(eggs)

sum = 0
for i in range(len(original_eggs)):
    if original_eggs[i] not in eggs:
        sum += original_eggs[i]

print(sum)