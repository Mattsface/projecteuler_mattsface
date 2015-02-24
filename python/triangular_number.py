#!/usr/bin/env python
"""
What is the value of the first triangle number to have over five hundred divisors?
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... there is a pattern here, so lets use it
28: 1,2,4,7,14,28
"""


def main():

    add_number = 2
    number = 3

    while True:
        prime_factors = find_prime_factors(number)
        primes = sort_primes(prime_factors)
        divisors = find_number_of_divisors(primes)

        if divisors >= 500:
            print number, divisors
            break

        add_number += 1
        number += add_number


def find_number_of_divisors(primes):
    """
    find the number of divisors
    """

    total = []
    for key, value in primes.items():
        total.append(value + 1)

    return reduce(lambda x, y: x * y, total)

def sort_primes(prime_factors):
    """
    create a dictionary of the prime numbers and the number of occurrences
    """
    primes = {}

    for n in prime_factors:
        if n in primes:
            continue
        n_occurrence = prime_factors.count(n)
        primes[n] = n_occurrence

    return primes

def find_prime_factors(n):
    """
    Find prime factors of n
    """

    i = 2
    factors = []

    while i * i <= n:
        if n % i:
            i += 1
        else:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    main()