"""solves this problem through brute force https://www.youtube.com/watch?v=vhp3d9XXDcQ """

from random import randint
import timeit

def get_num_rolls():

    #create counter for number of rolls
    counter = 0

    #loop until break condition
    while True:

        #get a roll
        roll = randint(1, 6)

        #if you roll a 6 -> return counter + 1
        if roll == 6:
            return counter + 1

        #otherwise, if roll is even -> good roll
        if roll == 2 or roll == 4:
            counter += 1

        #otherwise, restart
        else:
            counter = 0

#it is most certainly not equivalent
def perhaps_equivalent():
    counter = 0
    while True:
        roll = randint(1, 3)
        if roll == 3:
            return counter + 1
        else:
            counter += 1

def average_rolls(power):

    trials = int(2 ** power)

    roll_counter = 0

    for index in range(0, trials):
        #roll_counter += get_num_rolls()
        roll_counter += perhaps_equivalent()

    return float(roll_counter) / trials

print(average_rolls(16))

#print(min(timeit.Timer("get_num_rolls()", "from __main__ import get_num_rolls").repeat(10, 10000)))
