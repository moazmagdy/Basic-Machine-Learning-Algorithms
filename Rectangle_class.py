# -*- coding: utf-8 -*-
"""
This class accepts the length and width of a rectangle from the user and calculates the area of the rectangle.
"""
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
