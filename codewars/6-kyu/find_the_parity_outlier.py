def find_outlier(integers):
    evens = []
    odds = []
    for n in integers:
        if n % 2 == 1:
            odds.append(n)
        else:
            evens.append(n)
    
    
    if len(evens) == 1: return evens[0]
    else: return odds[0]