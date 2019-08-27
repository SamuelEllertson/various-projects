#!/usr/bin/env python

from sympy import isprime

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self):
        self.x, self.y = -self.y, self.x

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

def main():

    length = 100000

    ulamSpiral(length)

def ulamSpiral(length):
    
    #starting way out because my scatterplot script doesnt like negative x-values
    pos = Vector(10000, 0)
    direction = Vector(1, 0)

    limit = 1
    traveled = 0
    needsLimitIncrease = False

    for i in range(length):
        pos.add(direction)
        traveled += 1

        if isprime(i):
            print(pos.x, pos.y)

        if traveled == limit:
            traveled = 0
            direction.rotate()
            
            if needsLimitIncrease:
                limit += 1
                needsLimitIncrease = False
            else:
                needsLimitIncrease = True

if __name__ == '__main__':
    main()
