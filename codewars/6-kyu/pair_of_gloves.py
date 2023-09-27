def number_of_pairs(gloves):
    gloves_index = {}
    pairs = 0

    for glove in gloves:
        if glove in gloves_index.keys():
            gloves_index[glove] += 1
        else:
            gloves_index[glove] = 1

    print(gloves_index)
    
    for glove_type in gloves_index:
        # print(gloves_index[glove_type])
        if gloves_index[glove_type] % 2 == 0:
            # print('even')
            pairs += gloves_index[glove_type] / 2
        else:
            pairs += gloves_index[glove_type] // 2

    return int(pairs)

print(number_of_pairs(["red", "red", "red", "red", "red", "red"]))