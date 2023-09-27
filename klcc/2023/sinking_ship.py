def solve(coords):
    prev_coords = []
    coords = coords.split('\n')
    coords.remove('')

    for coord in coords:
            nums = coord.split(' ')
            for n in nums:
                if n.isdigit():
                    prev_coords.append(int(n))

a = """
2 3
3 2
10 10
"""

solve(a)