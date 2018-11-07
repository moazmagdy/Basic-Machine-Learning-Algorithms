# -*- coding: utf-8 -*-
"""
This class has two methods:
    1) get_string() : shows a prompt asking the user to enter a         string.
    2) print_string(): print the string entered by user.
"""

class strclass:

    def get_string(self):
        global string
        string = input('Please Enter a string: ')

    def print_string(self):
        print(string) 
            