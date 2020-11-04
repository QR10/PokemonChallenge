import pytest
from pokemon import get_grid_size, generate_grid

def test_get_grid_size_wrong_input() :
    x, y = get_grid_size("QwRtYuIp+-£$&£&")
    assert x == 0 and y == 0
    
def test_get_grid_size_long_input() :
    x, y = get_grid_size("eeeeeEEEEEeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\
                                 NNNNNNNNNNnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    assert x == 41 and y == 41
    
def test_get_grid_size_short_input() :
    x, y = get_grid_size("NSEO")
    assert x == 1 and y == 1
    

def test_generate_grid_out_of_range_x() :
    with pytest.raises(IndexError):
        grid = generate_grid(10, 0)
        grid[21][0]
        
def test_generate_grid_out_of_range_y() :
    with pytest.raises(IndexError):
        grid = generate_grid(0,20)
        grid[0][41]