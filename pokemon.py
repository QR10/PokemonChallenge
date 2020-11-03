# takes move sequence and returns dimensions for the grid
def get_map_size(ash_movement_sequence):

    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    down = 0
    up = 0
    right = 0
    left = 0
    
    while list_of_ash_movements:
        # retirar 1 movimento e processar
        ash_movement = list_of_ash_movements.pop()
    
        if ash_movement == "s":
            down += 1
        elif ash_movement == "n":
            up += 1
        elif ash_movement == "e":
            right +=1
        elif ash_movement == "o":
            left += 1
        else:
            # ignore wrong input
            print(f"{ash_movement} is not a valid move!")
    
    # Guardar maior numero de movimentos numa direcao
    if right > left:
        x = right
    else:
        x = left
        
    if down > up:
        y = down
    else:
        y = up
    
    return x, y
    
def generate_map(x, y) :
    # Generating 2d map according to movements
    world = []
    for j in range(x*2+1):
        column = []
        for i in range(y*2+1):
            column.append(1)
        world.append(column)
        
    # Ash starts here and gets starting Pokemon
    world[x][y] = 0 # center
        
    return world

def catch_pokemon(grid_of_houses, x, y):
    if grid_of_houses[x][y] == 1:
        grid_of_houses[x][y] = 0
        return 1
    else:
        return 0

def solve(ash_movement_sequence):
    x, y = get_map_size(ash_movement_sequence)
    
    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    grid_of_houses = generate_map(x, y) 

    pokemon_count = 1
    
    # Enquanto ouver movimentos
    while list_of_ash_movements:
        # retirar 1 movimento e processar
        ash_movement = list_of_ash_movements.pop()
    
        if ash_movement == "s":
            y = y+1
            pokemon_count += catch_pokemon(grid_of_houses, x, y)
        elif ash_movement == "n":
            y = y-1
            pokemon_count += catch_pokemon(grid_of_houses, x, y)
        elif ash_movement == "e":
            x = x+1
            pokemon_count += catch_pokemon(grid_of_houses, x, y)
        elif ash_movement == "o":
            x = x-1
            pokemon_count += catch_pokemon(grid_of_houses, x, y)
        else:
            # ignore wrong input
            print("Invalid move")
       
    # DEBUG Visual representation
    cols = len(grid_of_houses)
    rows = 0
    if cols:
        rows = len(grid_of_houses[0])
    for j in range(rows):
        for i in range(cols):
            print(grid_of_houses[i][j], end = "")
        print()
    
    print("Pokemon count is:", pokemon_count)
    
val = input("Enter Ash's movement sequence:")
solve(val)
#solve("NESSOONNNEEESSSSOOOONNNNNEEEEESSSSSSOOOOOONNNNNN")    