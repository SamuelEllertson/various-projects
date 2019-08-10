#!/usr/bin/env python

import random
import sys
import math
import functools

def main():
    length = 1000

    #sequence = reversedPrimes(length)
    sequence = [flyStraight(i) for i in range(length)]

    for val in sequence:
        print(val)

def primes(num):
    if 2 <= num:
        yield 2
    for i in range(3, num + 1, 2):
        if all(i % x != 0 for x in range(3, int(math.sqrt(i) + 1))):
            yield i

def reversedPrimes(length):
    sequence = []

    gen = primes(1000000)

    for _ in range(length):

        prime = gen.__next__()

        reversedP = int(bin(prime)[2:][::-1], 2)

        sequence.append(prime - reversedP)

    return sequence
        

@functools.lru_cache(maxsize=10000, typed=False)
def flyStraight(n):
    if n == 0 or n == 1:
        return 1

    previous = flyStraight(n-1)

    if(math.gcd(n, previous) == 1):
        return previous + n + 1
    return previous // math.gcd(n, previous)

if __name__ == '__main__':
    main()