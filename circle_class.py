# -*- coding: utf-8 -*-
"""
This class accepts the radius of a circle from user and has two methods to calculate the area and perimeter.
"""

class circle:
    def __init__(self, radius):
        self.radius = radius
    import math 
    def area(self):
        return math.pi * self.radius**2
    def perimeter(self):
        return math.pi * self.radius * 2