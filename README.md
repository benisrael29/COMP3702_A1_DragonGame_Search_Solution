# Assignment 1 

This is the submission code for COMP3702 2021 Assignment 1.


**game_env.py**

This file contains a class representing an Untitled Dragon Game level environment, storing the dimensions of the
environment, initial player position, exit position, number of gems and position of each gem, time limit, cost target,
the tile type of each grid position, and a list of all available actions.

This file contains a number of functions which will are used my solver:

~~~~~
__init__(filename)
~~~~~
Constructs a new instance based on the given input filename.


~~~~~
get_init_state()
~~~~~
Returns a GameState object (see below) representing the initial state of the level.


~~~~~
perform_action(state, action)
~~~~~
Simulates the outcome of performing the given 'action' starting from the given 'state', where 'action' is an element of
GameEnv.ACTIONS and 'state' is a GameState object. Returns a tuple (success, next_state), where success is True (if the
action is valid and does not collide) or False (if the action is invalid or collides), and next_state is a GameState
object.


~~~~~
is_solved(state)
~~~~~
Checks whether the given 'state' (a GameState object) is solved (i.e. all gems collected and player at exit). Returns
True (solved) or False (not solved).


~~~~~
is_game_over(state)
~~~~~
Checks whether the given 'state' (a GameState object) results in Game Over (i.e. player has landed on a lava tile).
Returns True (Game Over) or False (not Game Over).


~~~~~
render(state)
~~~~~
Prints a graphical representation of the given 'state' (a GameState object) to the terminal.


**game_state.py**

This file contains a class representing an Untitled Dragon Game state, storing the position of the player and the status
of all gems in the level (1 for collected, 0 for remaining).

~~~~~
__init__(row, col, gem_status)
~~~~~
Constructs a new GameState instance, where row and column are integers between 0 and n_rows, n_cols respectively, and
gem_status is a tuple of length n_gems, where each element is 1 or 0.


**play_game.py**

This file contains a script which launches an interactive game session when run. 

The script takes 2 command line arguments:
- input_filename, which must be a valid testcase file (e.g. one of the provided files in the testcases directory)
- (optional) output_filename, which should be an unused .txt filename

If an output filename is provided, the sequence of actions you perform will be saved as an output file.

When prompted for an action, type one of the available action strings (e.g. wr, wl, etc) and press enter to perform the
entered action.


**solution.py**

Template file for you to implement your solution to Assignment 1.

This file should include a 'main' method, allowing this file to be executed as a program from the command line.

Your program should accept 3 command line arguments:
    1) input filename
    2) output filename
    3) mode (either 'ucs' or 'a*')

We recommend you implement UCS first, then attempt A* after your UCS implementation is working.


**tester.py**

This file contains a script which tests whether the given output file is a valid solution to the given map file. You
should have a solution file produced by your solver before running the Tester script.

The script takes 2 command line arguments:
- input_filename, which must be a valid testcase file (e.g. one of the provided files in the testcases directory)
- output_filename, which should be the solution file written by your solver program

Use this script to evaluate your solution.


**visualiser.py**

This file contains a script which functions equivalently to the Tester script, but shows a visualisation of the state
after each action is performed. 

Like Tester, The script takes 2 command line arguments:
- input_filename, which must be a valid testcase file (e.g. one of the provided files in the testcases directory)
- output_filename

**testcases**

A directory containing input files which can be used to evaluate your solution.

The format of a testcase file is:
~~~~~
num_rows, num_cols
time_limit
cost_tgt
grid_data (row 1)
...
grid_data (row num_rows)
~~~~~

Testcase files can contain comments, starting with '#', which are ignored by the input file parser.