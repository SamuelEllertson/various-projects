#!/usr/bin/env python

from a import fermat_prime_test

def test_fermat_prime_test():
    
    for value in range(500):
        assert fermat_prime_test(value) == is_prime(value)

def is_prime(n):
    return n > 1 and all(n % i for i in range(2, n // 2 + 1))



if __name__ == '__main__':
    from py.test import main
    main()