import timeit
from helper import *


if __name__ == "__main__":

    """Performance benchmarking done here"""

    case = "ant_cube"

    if case == "testFunc":
        createNewSets()

    elif case == "sets":
        trials = 2**8
        print("creating new sets: " + test_performance(trials, "createNewSets"))
        print("clearing old sets: " + test_performance(trials, "clearOldSets"))

    elif case == "ant_cube":
        trials = 2**12
        print("attempt 1: " + test_performance(trials, "ant_cube_first_attempt"))
        print("attempt 2: " + test_performance(trials, "ant_cube_second_attempt"))
        print("attempt 3: " + test_performance(trials, "ant_cube_third_attempt"))
        print("attempt 4: " + test_performance(10, "ant_cube_fourth_attempt", trials//10))

    elif case == "binary_tree":
        trials = 2 ** 6
        print("insert: " + test_performance_2(trials, "test_insert", "tree, vals", get_setup("insert")))

