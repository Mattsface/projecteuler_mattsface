#!/usr/bin/env python
"""
Problem 8 on Project Euler Largest Product in a series

Find the thirteen adjacent digits in the 1000-digit number (largest_product.txt) that have the greatest product.
What is the value of this product?
"""

def main():
    f = open("largest_product.txt", 'r')
    numbers = f.read()
    f.close()

    find_number(numbers)

def find_number(numbers):
    """
    lets find that highest number
    """
    for n in numbers:
        print n


if __name__ == "__main__":
    main()