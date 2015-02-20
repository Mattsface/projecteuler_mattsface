#!/usr/bin/env python


def main():
    number = 600851475143

    factors = find_prime_factors(number)

    # dirty but I'm lazy ;)
    print int(factors[-1:][0])



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
