from preloaded import MORSE_CODE

# this doesnt work unless you run it in the kata enviornment
# https://www.codewars.com/kata/54b724efac3d5402db00065e
def decode_morse(morse_code):
    words = morse_code.strip().split("   ")
    
    decoded_words = []
    for word in words:
        letters = word.split(' ')
        temp = ''.join(MORSE_CODE[char] for char in letters)
        decoded_words.append(temp)
    
    result = ' '.join(decoded_words)
    
    return result

print(decode_morse('.... . -.--   .--- ..- -.. .'))