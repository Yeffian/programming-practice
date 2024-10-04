N = [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
jumps = 0
i = 0

while i < len(N):
    if N[i] == 1:
        jumps += 1
        # Skip consecutive 1s by incrementing i until we find a 0 or reach the end
        while i < len(N) and N[i] == 1:
            i += 1
    else:
        i += 1

print(jumps)
