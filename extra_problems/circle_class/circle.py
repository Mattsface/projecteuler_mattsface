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

    def __add__(self, other_circle):
        total_radius = self.radius + other_circle.radius
        return Circle(total_radius)

    def __mul__(self, int):
        total_radius = self.radius * int
        return Circle(total_radius)

    def __rmul__(self, other):
        if other == 0:
            return self
        else:
            return self.__mul__(other)




if __name__ == "__main__":
    c = Circle(3)
    assert c.diameter == 6
    assert c.radius == 3

    c = Circle.from_diameter(6)
    assert c.diameter == 6
    print c
    print repr(c)

    c1 = Circle(3)
    c2 = Circle(4)
    c3 = c1 + c2
    print repr(c3)
    c4 = c3 * 3
    print repr(c4)
    c5 = 3 * c4
    print repr(c5)