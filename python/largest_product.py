#!/usr/bin/env python
"""
Problem 8 on Project Euler Largest Product in a series

Find the thirteen adjacent digits in the 1000-digit number (largest_product.txt) that have the greatest product.

super ugly but it works!
"""


def main():
    f = open("largest_product.txt", 'r')
    numbers = f.read()
    f.close()
    numbers = numbers.replace('\n', '').replace('\r', '')
    #print numbers

    find_number(numbers)

def find_number(numbers):
    """
    lets find that highest number
    """


    x = 0
    y = 13
    final_total = 0
    for n in numbers:
        digits = numbers[x:y]
        array = []
        for digit in digits:
            array.append(int(digit))
        total = multiply_array(array)
        x += 1
        y += 1
        if total > final_total:
            final_total = total

    print final_total



def multiply_array(array_number):
    """
    return product of all the numbers in the array
    """
    total = 1

    for n in array_number:
        total *= n 

    return total

if __name__ == "__main__":
    main()