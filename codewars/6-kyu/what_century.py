import math

def ordinal(n):
    # idk wtf this is thank you stack overflow
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))

def what_century(year):
    century = 1 + (int(year) - 1) // 100
    return ordinal(century)
    
print(what_century("6700"))