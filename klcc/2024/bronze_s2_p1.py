def solve(n):
    c = 0
    for i in n:
        if i % 2 == 0:
            c += i
    return c

print(solve([22, 35, 5, -7, -25, -2, 31, -40, -33, -1, 36, -18, -11, 33, -47, 48, -20, -24, 41, -43, 8, 9, 12, 14, 50]))
print(solve([487, -631, 902, -759, 123, -214, 730, -812, 564, 291, -148, 456, 832, -925, 687, -451, 320, -117, 794, 921, -329, 604, -938, 481, -272, 110, 387, -659, 829, -502, 705, -799, 173, 258]))
print(solve([381, 496, 981, -849, -120, -777, 802, -743, 512, 130, -998, 124, 33, 601, 847, -222, -153, 403, -365, -766, 654, 900, -13, -600, 235, -176, -953, -78, 470, -579, -849, -622, 704, -852, 832, 102, -908, 186, 771, -36, -984, 450]))