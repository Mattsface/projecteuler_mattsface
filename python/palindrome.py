#!/usr/bin/env python

"""
A palindromic number reads the same both ways.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def main():
    large_pn = 0
    for x in range(100, 999):
        for y in range(100, 999):
            pn = x * y
            if str(pn) == str(pn)[::-1]:
                if pn > large_pn:
                    large_pn = pn

    print large_pn


if __name__ == "__main__":
    main()


