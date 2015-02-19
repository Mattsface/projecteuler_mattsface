#!/usr/bin/env python
"""
What is the value of the first triangle number to have over five hundred divisors?
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... there is a pattern here, so lets use it
28: 1,2,4,7,14,28
"""


def main():
    """
    add = 3
    number = 3
    triangle_number = 0
    while True:
        if find_divisors(number):
            print number
            break

        add += 1
        number += add
    """
    print find_largest_factor(20)

def find_largest_factor(n):
    i = 2

    # this doesn't work for perfect squares, lets fix it
    while i * i <= n:
        print i
        print n
        if n % i:   # because this return true if the number has a remander, we add one
            i += 1
        else:
            n //= i

    return n

if __name__ == "__main__":
    main()