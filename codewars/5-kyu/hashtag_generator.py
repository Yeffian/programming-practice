def generate_hashtag(s):
    if s == '':
        return False
    
    words = s.split()
    result = '#'

    for word in words:
        result += word.capitalize()

    if len(result) > 140:
        return False
    else:
        return result
    
print(generate_hashtag("    Hello     World   "  ))