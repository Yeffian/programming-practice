def get_count(sentence):
    result = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    for vowel in vowels:
        result += sentence.count(vowel)
    
    return result