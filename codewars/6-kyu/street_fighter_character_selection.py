# incomplete

def street_fighter_selection(fighters, initial_position, moves):
    result = []
    row = initial_position[0]
    col = initial_position[1]

    for move in moves:
        # not vertically circular
        if move == 'up':
            if fighters[row][col] in fighters[0]:
                result.append(fighters[row][col])
            else:
                row -= 1
                result.append(fighters[row][col])
        elif move == 'down':
            if fighters[row][col] in fighters[1]:
                result.append(fighters[row][col])
            else:
                row += 1
                result.append(fighters[row][col])
        # horizontally circular
        elif move == 'left':
            if col == 0:
                col = 5
                result.append(fighters[row][col])
            elif col == 5:
                col = 0   
                result.append(fighters[row][col])    
            else:
                col -= 1
                result.append(fighters[row][col])  
        elif move == 'right':
            if col == 0:
                col = 5
                result.append(fighters[row][col])
            elif col == 5:
                col = 0   
                result.append(fighters[row][col])
            else:
                col += 1
                result.append(fighters[row][col])

    return result

fighters = [
  ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
  ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

moves =  ["left"]*8
print(moves)
solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']

print(street_fighter_selection(fighters, (0, 0), moves))