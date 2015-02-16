#!/usr/bin/env


"""
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""

def main():
    total_sum = 0
    with open("numbers.txt") as fh:
        for line in fh:
            number = int(line.rstrip())
            total_sum += number

    print str(total_sum)[0:10]


if __name__ == "__main__":
    main()
