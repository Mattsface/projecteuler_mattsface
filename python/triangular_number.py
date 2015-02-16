#!/usr/bin/env python
"""
What is the value of the first triangle number to have over five hundred divisors?
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ... there is a pattern here, so lets use it
28: 1,2,4,7,14,28
"""


def main():

    add = 3
    number = 3
    triangle_number = 0
    while True:
        if find_divisors(number):
            print number
            break

        add += 1
        number += add

def find_divisors(number):
    divisors = []
    for n in range(1, number):
        if number % n == 0:
            divisors.append(n)

    if len(divisors) >= 500:
        return True



if __name__ == "__main__":
    main()