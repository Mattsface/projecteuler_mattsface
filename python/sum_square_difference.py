#!/usr/bin/env python
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():

    # The sum of the squares of the first 100 natural numbers is
    n2 = sum([ (x+1)**2 for x in range(0, 100)])

    # The square of the sum of the first 100 natural numbers is
    s = sum([ x + 1 for x in range(0, 100)])**2

    print s - n2

if __name__ == "__main__":
    main()