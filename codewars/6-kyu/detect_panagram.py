from string import ascii_lowercase

def is_pangram(s):
    for letter in ascii_lowercase:
        if letter not in s.lower():
            return False
    return True