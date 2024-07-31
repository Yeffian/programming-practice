def first_non_repeating_letter(s):
    lower_s = s.lower()
    char_count = {}

    for char in lower_s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for i, char in enumerate(s):
        if char_count[lower_s[i]] == 1:
            return char

    return ""