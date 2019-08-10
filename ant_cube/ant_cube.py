"""simulation to answer https://www.youtube.com/watch?v=dDrhWQVLdL8"""

from random import randint
import timeit

def ant_cube_first_attempt():
    """runs an ant_cube simulation, returns true on collision, false otherwise"""
    cube = []

    for x in range(0, 8):
        x = ("000" + bin(x)[2:])[-3:]
        cube.append(x)

    for index in range(0, 8):
        path = randint(0, 2)
        ant = cube[index]
        ant = ant[0:path] + str(int(ant[path]) ^ 1) + ant[path+1:]
        cube[index] = ant

    testSet = set()

    for ant in cube:
        testSet.add(ant)

    if len(testSet) == 8:
        return False
    else:
        return True


def ant_cube_test_first_attempt(rounds):
    """runs ant_cube simulation many times and calculates probability"""
    collisions = 0
    for i in range(0,rounds):
        if(ant_cube_first_attempt()):
            collisions += 1

    return float(collisions) / rounds 

def ant_cube_second_attempt():
    cube = [0b000, 0b001, 0b010, 0b011, 0b100, 0b101, 0b110, 0b111]
    masks = [0b001, 0b010, 0b100]

    for index in range(0, 8):
        rand = randint(0, 2)
        cube[index] ^= masks[rand]

    test_set = set()

    for ant in cube:
        test_set.add(ant)

    if len(test_set) == 8:
        return False
    else:
        return True

def ant_cube_test_second_attempt(rounds):
    """runs ant_cube simulation many times and calculates probability"""
    collisions = 0
    for i in range(0,rounds):
        if(ant_cube_second_attempt()):
            collisions += 1

    return float(collisions) / rounds

def ant_cube_third_attempt():
    masks = [0b001, 0b010, 0b100]
    newSet = set()
    for index in range(0, 8):
        ant = index ^ masks[randint(0, 2)]
        newSet.add(ant)
    if len(newSet) == 8:
        return False
    return True

def ant_cube_test_third_attempt(rounds):
    """runs ant_cube simulation many times and calculates probability"""
    collisions = 0
    for i in range(0,rounds):
        if(ant_cube_third_attempt()):
            collisions += 1

    return float(collisions) / rounds

def ant_cube_fourth_attempt(trials):
    masks = [0b001, 0b010, 0b100]
    newSet = set()
    collisions = 0

    for trial in range(0, trials):

        newSet.clear()

        for index in range(0, 8):
            ant = index ^ masks[randint(0, 2)]
            newSet.add(ant)

        if len(newSet) != 8:
            collisions += 1
    
    return collisions / trials



#print(1 - ant_cube_test_first_attempt(100000))
#print(1 - ant_cube_test_second_attempt(100000))
#print(1 - ant_cube_test_third_attempt(100000))
#print(1 - ant_cube_fourth_attempt(100000))


#print(min(timeit.Timer("ant_cube_second_attempt()", "from __main__ import ant_cube_second_attempt").repeat(10, 10000)))
print(min(timeit.Timer("ant_cube_fourth_attempt(10)", "from __main__ import ant_cube_fourth_attempt").repeat(10, 1000)))