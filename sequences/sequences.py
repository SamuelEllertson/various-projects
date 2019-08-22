#!/usr/bin/env python
"""
Implementation of sequences from this Numberphile series: https://www.youtube.com/playlist?list=PLt5AfwLFPxWLkoPqhxvuA8183hh1rBnGM
"""

import random
import sys
import math
import functools

def main():
    length = 1000
    shouldPrint = True

    #sequence = [flyStraight(i) for i in range(length)]
    #sequence = reversedPrimes(length)
    #sequence = [balancedTernary(i) for i in range(length)]
    #sequence = [wisteria(i) for i in range(1, length)]
    #sequence = forestFire(length)
    #sequence = [stern(i) for i in range(length)]
    #sequence = [hofstadters(i) for i in range(length)]
    sequence = [sigrist(i) for i in range(1, length)]

    if shouldPrint:
        for val in sequence:
            print(val)

@functools.lru_cache(maxsize=100000, typed=False)
def sigrist(n):
    
    if n <= 1:
        return 0

    unavailable = []

    for i in range(n):
        if i & n:
            unavailable.append(sigrist(i))

    for i in infinity(start=0):
        if i not in unavailable:
            return i


@functools.lru_cache(maxsize=100000, typed=False)
def hofstadters(n):
    #a(n) = a(n - a(n-1)) + a(n - a(n-2))

    if n <= 1:
        return 1

    return hofstadters(n - hofstadters(n-1)) + hofstadters(n - hofstadters(n-2))


@functools.lru_cache(maxsize=10000, typed=False)
def stern(n):
    #a(2*n) = a(n), a(2*n+1) = a(n) + a(n+1)

    if n <= 1:
        return n

    if n % 2 == 0:
        return stern(n//2)
    return stern((n-1)//2) + stern((n+1)//2)

def forestFire(length):
    #a[i+j] - a[i] != a[i+2j] - a[i+j]

    a = []

    for i in range(length):

        for smallest in infinity():
            if works(a, smallest):
                a.append(smallest)
                break

    return a

def works(a, value):

    ln = len(a)

    if ln < 2:
        return True

    index = ln
    step = 1

    while True:

        if step * 2 > ln:
            return True

        if value - a[index - step] == a[index - step] - a[index - 2 * step]:
            return False

        step += 1

    return True
 
def infinity(start=1, increment=1):
    val = start
    while True:
        yield val
        val += increment

def wisteria(num):
    numString = str(num)

    product = 1
    for digit in numString:
        value = int(digit)

        if value != 0:
            product *= value

    return num - product

def balancedTernary(num):
    ternary = baseConvert(num, 3)

    total = 0
    base = 1

    for digit in ternary[::-1]:
        
        if digit == "0":
            pass
        if digit == "1":
            total += base 
        if digit == "2":
            total -= base

        base *= 3

    return total

def baseConvert(n, base):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    try:
        n = int(n)
        base = int(base)
    except:
        return ""

    if n < 0 or base < 2 or base > 36:
        return ""

    s = ""

    while 1:
        r = n % base
        s = digits[r] + s
        n = n // base
        if n == 0:
            break

    return s

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