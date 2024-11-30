from itertools import chain

def solve(e):
    e_d = dict()
    for entity in e:
        e_d[entity[0]] = entity[1]
    print(e_d)
    names = sorted(e_d, reverse=True)
    print(names)


solve([["Banshee", 5], ["Wraith", 8], ["Ghost", 3], ["Vampire", 7], ["Zombie", 4]])