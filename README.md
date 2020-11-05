# Pokemon Challenge

Given a sequence of movements the script calculates the number of pokemons caught by Ash on that journey.

Given that each house as only 1 pokemon to catch, if Ash catches the pokemon and comes back to that same house, there won't be a pokemon there anymore.
Ash always starts in one house and catches it's first pokemon, he then moves according to the sequence. 


![Pokemon](Media/pokemon.gif)


# Requirements

## To run this code follow the following steps:

### Have Python 3 installed on your machine

- Download Python: https://www.python.org/downloads/

#### OR

### Install Anaconda

Anaconda is a free and open source distribution of the Python and R programming languages for large-scale data processing, predictive analytics, and scientific computing, that aims to simplify package management and deployment.

[More Info...](https://www.anaconda.com/)

[Download and Install Anaconda](https://www.anaconda.com/products/individual)



### Install Git 

https://git-scm.com/downloads


### Create a new directory somewhere, and clone the project by running the following line on your terminal/cmd:
```
git clone https://github.com/QR10/PokemonChallenge
```


### To run the script type the following line on your terminal/cmd:
```
python pokemon.py
```

## To run the tests the following steps are required:

#### Install the pytest framework by running the following line on your terminal/cmd:
```
pip install -U pytest
```
[For more Infor refer to...](https://docs.pytest.org/en/stable/getting-started.html)

#### Open a terminal/cmd in the test script location and execute the following line:
```
pytest
```
![Pytest](Media/pytest.png)
