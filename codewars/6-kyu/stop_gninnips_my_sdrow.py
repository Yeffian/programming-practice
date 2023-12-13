def spin_words(sentence):
    if len(sentence) == 0:
        return None
    
    result = []
    words = sentence.split(" ")

    for word in words:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)

    return " ".join(word for word in result)
          
print(spin_words("Hey fellow warriors"))