#!/usr/bin/env python

"""Module for fermat primarily test"""

from random import randrange
from math import gcd

def fermat_prime_test(value, confidence=100):
    """Runs the fermat primality algorithm to check if value is prime

    Parameters:
        value (int): The value to check for primality
        confidence (int): The number of times to run the test. Higher means more confident.

    Returns:
        bool: True if value is a prime, False otherwise.

    Examples:
        >>> fermat_prime_test(7)
        True
        >>> fermat_prime_test(51)
        False
        >>> fermat_prime_test(10)
        False
    """

    if value < 2:
        return False

    stream = iter(coprime_stream(value))

    for _ in range(confidence):
        coprime_value = next(stream)

        if pow(coprime_value, value-1, value) != 1:
            return False

    return True

def coprime_stream(value):
    """Generates a stream of random numbers that are coprime to value

    Arguments:
        value {int} -- The value all yielded values are coprime to.

    Yields:
        int -- a random value coprime to value. Size is between 0 and value.
    """
    while True:
        coprime = randrange(value)
        if gcd(coprime, value) == 1:
            yield coprime

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
