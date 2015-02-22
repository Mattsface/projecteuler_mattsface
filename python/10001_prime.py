#!/bin/usr/env

import sys

def main():
    n = 100000

    while True:

        binary_array, primes = [True] * (n+1), []
        for p in xrange(2, n+1):
            # if b[p] is true, we append to ps
            # because p is 2, and prime we apply it
            if binary_array[p]:
                primes.append(p)
                for i in xrange(p, n+1, p):
                    binary_array[i] = False


        if len(primes) > 10002:
            print primes[10000]
            break
        print n
        n = n * 2



if __name__ == "__main__":
    main()
