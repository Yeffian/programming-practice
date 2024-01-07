def words_to_object(s):
    if s == "": return "[]"
    result = "["

    parts = s.split(' ')
    for i, (k, v) in enumerate(zip(parts[0::2], parts[1::2])):
        if len(list(zip(parts[0::2], parts[1::2]))) == 1: 
            return "[{name : '" + parts[0] + "', id : '" + parts[1] + "'}]"
        elif i == 0: 
            item = "{name : '" + k + "', id : '" + v + "'}, "
        elif i == len(list(zip(parts[0::2], parts[1::2]))) - 1:
            item = "{name : '" + k + "', id : '" + v + "'}"
        else:
            item = "{name : '" + k + "', id : '" + v + "'}, "
        result += item
    
    result += "]"
    return result

print(words_to_object("red 1"))