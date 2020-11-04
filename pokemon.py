def get_grid_size(ash_movement_sequence):
    """ Returns the maximum used X and Y axis sizes for a movement sequence
    as 2 integers.
    
    Expects: A string with a sequence of movements
    Modifies: Nothing
    Returns: Two integers, X-axis value and Y-axis value
   
    """
    
    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    south_moves = 0
    north_moves = 0
    east_moves = 0
    west_moves = 0
    
    while list_of_ash_movements:
        ash_movement = list_of_ash_movements.pop()
    
        if ash_movement == "s":
            south_moves += 1
        elif ash_movement == "n":
            north_moves += 1
        elif ash_movement == "e":
            east_moves +=1
        elif ash_movement == "o":
            west_moves += 1
        else:
            print(f"{ash_movement} is not a valid move!")
    
    # Guardar maior numero de movimentos numa direcao
    if east_moves > west_moves:
        x = east_moves
    else:
        x = west_moves
        
    if south_moves > north_moves:
        y = south_moves
    else:
        y = north_moves
    
    return x, y
    
def generate_grid(x, y) :
    """Returns a grid full of pokemons to catch, with the exception of the
    starting pokemon/house.
    
    Expects: X and Y axis max values as integers
    Modifies: Nothing 
    Returns: A grid full of pokemons to catch
    
    """
    world = []
    for j in range(x*2+1):
        column = []
        for i in range(y*2+1):
            column.append(1)
        world.append(column)
        
    # Ash starts here and gets starting Pokemon
    world[x][y] = 0
        
    return world

def catch_pokemon(grid_of_houses, x, y):
    """ Returns an integer with the number of pokemons caught in Ash's
    current position.
    
    Expects: Grid with houses and x and y coordinates of ash's position
    Modifies: Number of available pokemons in the current house
    Returns: An integer with number of pokemons caught
    """
    
    if grid_of_houses[x][y] == 1:
        grid_of_houses[x][y] = 0
        return 1
    else:
        return 0

def solve(ash_movement_sequence):
    """Prints the amount of pokemons caught by Ash in a user specified 
    movement sequence.
    
    Expects: A string with Ash's movement sequence
    Modifies: Nothing
    Returns: Nothing
    """
    x, y = get_grid_size(ash_movement_sequence)
    
    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    grid_of_houses = generate_grid(x, y) 

    pokemon_count = 1
    
    while list_of_ash_movements:
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
    
    print(f"Ash caught {pokemon_count} pokemons")
    
user_move_sequence = input("Enter Ash's movement sequence:")
solve(user_move_sequence)