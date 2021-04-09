# Conway's Game of Life 

The Game of Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. The game is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input.
![image](https://github.com/majohdezo/ConwayGoL/blob/master/Files/GoL_Sim.gif)

## Instructions:

`Language: Python 3.8.2`

### Libraries used
```
Numpy: pip install numpy
Matplotlib: pip install matplotlib
```

### Input
This program needs a txt file.  The correct format to use it is at the first line, in the first column you write the `Universe size`, then a blank space and in the second column the `number of Generations`; then clik enter without empty lines, and from now the first column is the `X`coordinate, then a blank space, and the second column means the `Y`coordinate of each alive cell.

At `line 17`it is necessary to type the txt [file](https://github.com/majohdezo/ConwayGoL/blob/master/Test.txt)  name to begin the simulation. Once the simulation is completed, you will see another [txtFile](https://github.com/majohdezo/ConwayGoL/blob/master/Results.txt) with the results of the simulations and the incidence percentage of each configuration.

### Other inputs:
If you want to create a random simulation, you can try removing the comments at lines `416, 417 and 425`. G belongs to the `number of Generations`, N to the `Universe size` and line 425 creates the random grid with these values.

## References:
This code was based on this [file](https://github.com/gcastillo56/com139-class/blob/master/GoL/conway.py) 
