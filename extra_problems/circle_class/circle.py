#!/usr/bin/env python
from math import *



class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        c = cls(radius)
        return c

    def __str__(self):
        return "Circle with radius {}".format(self.radius)

    def __repr__(self):
        return "Circle({})".format(self.radius)



if __name__ == "__main__":
    c = Circle(3)
    assert c.diameter == 6
    assert c.radius == 3

    c = Circle.from_diameter(6)
    assert c.diameter == 6
    print c
    print repr(c)
