
"""
game_state.py

This file contains a class representing an Untitled Dragon Game state. You should make use of this class in your solver.

COMP3702 2021 Assignment 1 Support Code

Last updated by njc 27/07/21
"""
import game_env as game_env

class GameState:
    """
    Instance of an Untitled Dragon Game state. row and col represent the current player position. gem_status is 1 for
    each collected gem, and 0 for each remaining gem.

    You may use this class and its functions. You may add your own code to this class (e.g. get_successors function,
    get_heuristic function, etc), but should avoid removing or renaming existing variables and functions to ensure
    Tester functions correctly.
    """

    def __init__(self, row, col, gem_status):
        self.row = row
        self.col = col
        assert isinstance(gem_status, tuple), '!!! gem_status should be a tuple !!!'
        self.gem_status = gem_status
        self.actions= []
        self.pathcost = 0

    def __eq__(self, other):
        if not isinstance(other, GameState):
            return False
        return self.row == other.row and self.col == other.col and self.gem_status == other.gem_status

    def __hash__(self):
        return hash((self.row, self.col, *self.gem_status))

    def deepcopy(self):
        return GameState(self.row, self.col, self.gem_status)

    # Returns a list of all the possible actions. 
    def get_sucessors(self, game_enviroment):
        sucessors = []
        for action in game_enviroment.ACTIONS:
            if game_enviroment.perform_action(self, action) != (False, self):
                boolean, next_state = game_enviroment.perform_action(self, action)
                cost_of_action = game_enviroment.ACTION_COST.get(action)
                sucessors.append([next_state, cost_of_action, action])
        return sucessors
        
    def add_action(self, action):
        self.actions.append(action)
    
    #Will return a value associated with distance to a gem. 
    def get_heuristic(self, game_enviroment):
        if game_enviroment.n_gems !=0:
            distances = []
            for position in game_enviroment.gem_positions:
                x,y  = position[0], position [1]
                dx = abs(x - self.row)
                dy = abs(y - self.col)
                distances.append (dx + dy)
            return min(distances)
        
        if game_enviroment.n_gems == 0:
            x,y = game_enviroment.exit_row, game_enviroment.exit_col
            dx = abs(x - self.row)
            dy = abs(y - self.col)
            return dy + dx
            
