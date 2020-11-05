import pytest
import pokemon

def test_get_grid_size_wrong_input() :
    x, y = pokemon.get_grid_size("QwRtYuIp+-£$&£&")
    assert x == 0 and y == 0
    
def test_get_grid_size_long_input() :
    x, y = pokemon.get_grid_size("eeeeeEEEEEeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\
                                 NNNNNNNNNNnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    assert x == 41 and y == 41
    
def test_get_grid_size_short_input() :
    x, y = pokemon.get_grid_size("NSEO")
    assert x == 1 and y == 1
    

def test_generate_grid_out_of_range_x() :
    with pytest.raises(IndexError):
        grid = pokemon.generate_grid(10, 0)
        grid[21][0]
        
def test_generate_grid_out_of_range_y() :
    with pytest.raises(IndexError):
        grid = pokemon.generate_grid(0,20)
        grid[0][41]
        
def test_catch_a_pokemon_pokemon_found() :
    grid = pokemon.generate_grid(2,2)
    assert pokemon.catch_a_pokemon(grid, 0, 0) == 1
    
def test_catch_a_pokemon_pokemon_found_and_caught() :
    grid = pokemon.generate_grid(2,2)
    pokemon.catch_a_pokemon(grid, 0, 0)
    assert pokemon.catch_a_pokemon(grid, 0, 0) == 0

def test_catch_a_pokemon_pokemon_not_found() :
    grid = pokemon.generate_grid(4,4)
    assert pokemon.catch_a_pokemon(grid, 4, 4) == 0
    
def test_count_pokemons_caught_1() :
    grid = pokemon.generate_grid(2,2)
    assert pokemon.count_pokemons_caught("SOON", grid, 2, 2) == 5
    
def test_count_pokemons_caught_2() :
    grid = pokemon.generate_grid(10,10)
    move_sequence = "nsnsnsnsnsnsnsnsnsnsoeoeoeoeoeoeoeoeoeoe"
    assert pokemon.count_pokemons_caught(move_sequence, grid, 10, 10) == 3
    
def test_count_pokemons_caught_3() :
    x, y = pokemon.get_grid_size("")
    grid = pokemon.generate_grid(x,y)
    assert pokemon.count_pokemons_caught("", grid, x, y) == 1
    
def test_count_pokemons_caught_4() :
    move_sequence = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\
        nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn\
        nnooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
        ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\
        oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooosssssssss\
        sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss\
        sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss\
        ssssssssssssssssssssssssssssssssssssssssssssssssseeeeeeeeeeeeeeeeeeee\
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\
        eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"
    x, y = pokemon.get_grid_size(move_sequence)
    grid = pokemon.generate_grid(x,y)
    assert pokemon.count_pokemons_caught(move_sequence, grid, x, y) == 784
    
def test_play_pokemon_1(capsys) :
    pokemon.play_pokemon("S");
    captured = capsys.readouterr()
    assert captured.out == "O Ash apanhou 2 pokémons!\n"

def test_play_pokemon_2(capsys) :
    pokemon.play_pokemon("NeSo");
    captured = capsys.readouterr()
    assert captured.out == "O Ash apanhou 4 pokémons!\n"
    
