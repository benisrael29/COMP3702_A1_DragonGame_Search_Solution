import sys

from game_env import GameEnv

"""
Tester script.

Use this script to evaluate your solution. You may modify this file if desired. When submitting to GradeScope, an
unmodified version of this file will be used to evaluate your code.

You may import methods from this file into your solution if you wish.

COMP3702 2021 Assignment 1 Support Code

Last updated by njc 05/08/21
"""


def main(arglist):
    if len(arglist) != 2:
        print("Running this file tests whether the given output file is a valid solution to the given map file.")
        print("Usage: tester.py [input_filename] [output_filename]")
        return -1

    input_file = arglist[0]
    output_file = arglist[1]

    game_env = GameEnv(input_file)

    try:
        f = open(output_file, 'r')
    except FileNotFoundError:
        return 255
    actions = f.readline().strip().split(',')

    # apply each action in sequence
    persistent_state = game_env.get_init_state()
    total_cost = 0
    error_occurred = False
    for i in range(len(actions)):
        a = actions[i]
        total_cost += game_env.ACTION_COST[a]
        success, persistent_state = game_env.perform_action(persistent_state, a)
        if not success:
            print("ERROR: Action resulting in Collision performed at step " + str(i))
            error_occurred = True
        elif game_env.is_game_over(persistent_state):
            print("ERROR: Action resulting in Game Over performed at step " + str(i))
            error_occurred = True

    if error_occurred:
        return 255

    if game_env.is_solved(persistent_state):
        print("Level completed!")
        if abs(total_cost - game_env.cost_tgt) < 1e-5:
            print(f"Solution is optimal (total cost = {round(total_cost, 1)})!")
            return 0
        else:
            print(f"Solution cost is {round(total_cost, 1)} (optimal cost = {game_env.cost_tgt})")
            return int(total_cost - game_env.cost_tgt)
    else:
        print("ERROR: Level not completed after all actions performed.")
        return 255


if __name__ == '__main__':
    ret = main([sys.argv[1:]])
    sys.exit(ret)
