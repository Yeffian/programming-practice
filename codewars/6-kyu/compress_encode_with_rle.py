def encode(inp):
    inp += ' '
    current = ''
    num = 0
    result = ''
    for letter in inp:
        if current == letter:
            num += 1
        else:
            result += f'{current}{num}'
            current = letter
            num = 1
    return result.replace(result[0], '')


print(encode("HELLO WORLD"))