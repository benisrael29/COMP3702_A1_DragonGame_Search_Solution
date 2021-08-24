import sys
import os

from game_env import GameEnv
from game_state import GameState
import heapq
import queue as queuelib
import itertools
import time

"""
solution.py

Template file for you to implement your solution to Assignment 1.

This file should include a 'main' method, allowing this file to be executed as a program from the command line.

Your program should accept 3 command line arguments:
    1) input filename
    2) output filename
    3) mode (either 'ucs' or 'a_star')

COMP3702 2021 Assignment 1 Support Code

Last updated by njc 04/08/21
"""


#
#
# Code for any classes or functions you need can go here.
#
#



"""
Uniform cost search algo

"""
def ucs(env, state):
    " Queue is established as: weighting , tie_resolve counter, state object"
    fringe = queuelib.PriorityQueue()
    counter = itertools.count()
    fringe.put((0, next(counter), state))
    # dict: state --> path_cost
    visited = {state: 0}
    action_dic = {state: []}
    c= itertools.count()
    n_expanded = 0
    
    while not fringe.empty():
        n_expanded +=1
        _, __, node = fringe.get()
        # check if this state is the goal
        if env.is_solved (node):
            print("UCS, Visited Nodes: %d, Expanded Nodes: %d, Cost of Path: %d" %( len(visited.keys()), n_expanded, visited[node]))
            return action_dic[node]
        
        #print(next(c))
        # add unvisited (or visited at higher path cost) successors to container
        successors = node.get_sucessors(env)

        for a_state in successors:
            state_obj = a_state[0]
            cost_of_action = a_state[1]
            action = a_state[2]
            cost_so_far = node.pathcost + cost_of_action
            
            if state_obj not in visited.keys():
                state_obj.path_cost = cost_so_far
                visited[state_obj] = state_obj.path_cost
                action_dic[state_obj] = action_dic[node] + [action]
                fringe.put((state_obj.path_cost, next(counter), state_obj))
    return None 

def getStateid (row, col):
    return "%s,%s" %(row, col)

def a_star(env, state):
    fringe = queuelib.PriorityQueue()
    counter = itertools.count()
    fringe.put((0, next(counter), state))

    # dict: state --> path_cost
    initial_id=getStateid(state.row, state.col)

    visited = {initial_id: 0}
    action_dic = {initial_id: []}
    nodes = []
    n_expanded = 0
    while not fringe.empty():
        n_expanded +=1
        #state obj, cost of action , action 
        _, __, node = fringe.get()

        node_id = getStateid (node.row, node.col)
        # check if this state is the goal
        if env.is_solved (node):
            print("A-star, Visited Nodes: %d, Expanded Nodes: %d, Cost of Path: %d" % ( len(visited.keys()), n_expanded, visited[node_id] ))
            return action_dic[node_id]


        # add unvisited (or visited at higher path cost) successors to container
        successors = node.get_sucessors(env)

        for a_state in successors:
            state_obj = a_state[0]
            nodes.append(state_obj)
            state_id = getStateid(state_obj.row, state_obj.col)
            cost_of_action = a_state[1]
            action = a_state[2]
            cost_to_go = visited[node_id] + cost_of_action


            if state_id not in visited.keys() or cost_to_go < visited.get(state_id):
                visited[state_id] = cost_to_go
                action_dic[state_id] = action_dic[node_id] + [action]
                stack_weight = visited[state_id] + state_obj.get_heuristic(env)      
                fringe.put((stack_weight, next(counter), state_obj))
        
        for node in nodes:
            node_id = getStateid(node.row, node.col)
            if env.is_solved(node):
                return action_dic[node_id]
    return action_dic[node_id]




def write_output_file(filename, actions):
    """
    Write a list of actions to an output file.
    :param filename: name of output file
    :param actions: list of actions where is action an element of GameEnv.ACTIONS
    """
    f = open(filename, 'w')
    for i in range(len(actions)):
        f.write(str(actions[i]))
        if i < len(actions) - 1:
            f.write(',')
    f.write('\n')
    f.close()


def main(arglist):
    if len(arglist) != 3:
        print("Running this file launches your solver.")
        print("Usage: play_game.py [input_filename] [output_filename] [mode = 'ucs' or 'a*']")

    input_file = arglist[0]
    output_file = arglist[1]
    mode = arglist[2]

    assert os.path.isfile(input_file), '/!\\ input file does not exist /!\\'
    assert mode == 'ucs' or mode == 'a_star', '/!\\ invalid mode argument /!\\'

    # Read the input testcase file
    game_env = GameEnv(input_file)
    initial_state = game_env.get_init_state()

    actions = []

    if mode == 'ucs':
        actions = ucs(game_env, initial_state )

        
    if mode == 'a_star':
        actions = a_star(game_env, initial_state)


    # Write the solution to the output file
    write_output_file(output_file, actions)


if __name__ == '__main__':
    ret = main(sys.argv[1:])

