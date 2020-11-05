def get_grid_size(ash_movement_sequence):
    """ Returns the maximum used X and Y axis sizes for a movement sequence
    as 2 integers.
    
    Expects: A string with a sequence of movements
    Modifies: Nothing
    Returns: Two integers, X-axis value and Y-axis value
   
    """
    
    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    south_movements_count = 0
    north_movements_count = 0
    east_movements_count = 0
    west_movements_count = 0
    
    while list_of_ash_movements:
        move_ash = list_of_ash_movements.pop()
    
        if move_ash == "s":
            south_movements_count += 1
        elif move_ash == "n":
            north_movements_count += 1
        elif move_ash == "e":
            east_movements_count +=1
        elif move_ash == "o":
            west_movements_count += 1
        else:
            print(f"{move_ash} não é um movimento valido!")
    
    # Guardar maior numero de movimentos numa direcao
    if east_movements_count > west_movements_count:
        x_axis_movements = east_movements_count
    else:
        x_axis_movements = west_movements_count
        
    if south_movements_count > north_movements_count:
        y_axis_movements = south_movements_count
    else:
        y_axis_movements = north_movements_count
    
    return x_axis_movements, y_axis_movements
    
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

def catch_a_pokemon(grid_of_houses, x, y):
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

def count_pokemons_caught(ash_movement_sequence, grid_of_houses, x_axis_pos,
                              y_axis_pos) :
    """ Counts the number of pokemons caught by ash in a given move sequence
    and returns the count as an integer
    
    Expects: A string with a list of moves, a grid filled with pokemons to
        catch, ash's x-axis and y-axis starting position'
    Modifies: Nothing
    Returns: A count of pokemons caught, as an integer 
    """    
    list_of_ash_movements = list(ash_movement_sequence.lower())[::-1]
    
    # Starting house pokemon acquired
    pokemon_caught_count = 1
    
    while list_of_ash_movements:
        move_ash = list_of_ash_movements.pop()
    
        if move_ash == "s":
            y_axis_pos = y_axis_pos+1
            pokemon_caught_count += catch_a_pokemon(grid_of_houses, 
                                                      x_axis_pos, y_axis_pos)
        elif move_ash == "n":
            y_axis_pos = y_axis_pos-1
            pokemon_caught_count += catch_a_pokemon(grid_of_houses,
                                                      x_axis_pos, y_axis_pos)
        elif move_ash == "e":
            x_axis_pos = x_axis_pos+1
            pokemon_caught_count += catch_a_pokemon(grid_of_houses,
                                                      x_axis_pos, y_axis_pos)
        elif move_ash == "o":
            x_axis_pos = x_axis_pos-1
            pokemon_caught_count += catch_a_pokemon(grid_of_houses,
                                                      x_axis_pos, y_axis_pos)
    
    return pokemon_caught_count

def play_pokemon(ash_movement_sequence):
    """Prints the amount of pokemons caught by Ash in a user specified 
    movement sequence.
    
    Expects: A string with Ash's movement sequence
    Modifies: Nothing
    Returns: Nothing
    """
    x_axis_position, y_axis_position = get_grid_size(ash_movement_sequence)
    
    grid_of_houses = generate_grid(x_axis_position, y_axis_position) 

    pokemons_caught_count = count_pokemons_caught(ash_movement_sequence,
                                               grid_of_houses, x_axis_position,
                                                 y_axis_position)
    
    print(f"O Ash apanhou {pokemons_caught_count} pokémons!")

def main():
    user_move_sequence = input("Insira a sequência de movimentos do ash: ")
    play_pokemon(user_move_sequence)

if __name__ == "__main__":
    main()
    