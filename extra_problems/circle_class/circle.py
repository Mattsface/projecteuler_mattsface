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

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

