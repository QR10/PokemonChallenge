# takes move sequence and returns dimensions for the grid
def numOfMovements(moveSequence):
    # Turn string into a list of characters
    movements = list(moveSequence.lower())[::-1]
    
    down = 0
    up = 0
    right = 0
    left = 0
    
    # Enquanto ouver movimentos
    while movements:
        # retirar 1 movimento e processar
        move = movements.pop()
    
        if move == "s":
            # move down
            down += 1
        elif move == "n":
            # move up
            up += 1
        elif move == "e":
            # move right
            right +=1
        elif move == "o":
            # move left
            left += 1
        else:
            # ignore wrong input
            print("Invalid move")
    
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
    
def solve(moveSequence):
    x, y = numOfMovements(moveSequence)
    
    # String to list of characters 
    movements = list(moveSequence.lower())[::-1]
    
    # Generating 2d World according to movements
    world = []
    for j in range(x*2):
        column = []
        for i in range(y*2):
            column.append(1)
        world.append(column)
        
    # Ash starts here and gets starting Pokemon
    world[x][y] = 0 # center
    pokeCount = 1
    
    # Enquanto ouver movimentos
    while movements:
        # retirar 1 movimento e processar
        move = movements.pop()
    
        if move == "s":
            # move down
            y = y+1
            if world[x][y] == 1:
                world[x][y] = 0
                pokeCount += 1
        elif move == "n":
            # move up
            y = y-1
            if world[x][y] == 1:
                world[x][y] = 0
                pokeCount += 1
        elif move == "e":
            # move right
            x = x+1
            if world[x][y] == 1:
                world[x][y] = 0
                pokeCount += 1
        elif move == "o":
            # move left
            x = x-1
            if world[x][y] == 1:
                world[x][y] = 0
                pokeCount += 1
        else:
            # ignore wrong input
            print("Invalid move")
       
    # DEBUG Visual representation
    cols = len(world)
    rows = 0
    if cols:
        rows = len(world[0])
    for j in range(rows):
        for i in range(cols):
            print(world[i][j], end = "")
        print()
    
    print("Pokecount is:", pokeCount)
    
val = input("Enter Ash's movement sequence:")
solve("NESSOONNNEEESSSSOOOONNNNNEEEEESSSSSSOOOOOONNNNNN")    