# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:00:10 2018

@author: moazm
"""

from flask import Flask
app = Flask(__name__)

import math
@app.route('/')
def home_page():
    return 'Please Enter the Circle radius in mm'

@app.route('/<int:radius>')
def area(radius):
    return 'Circle area = ' + format(math.pi*radius**2, '.2f') + ' and Circle perimeter = ' + format(2*math.pi*radius, '.2f')

if __name__ == '__main__':
    app.run(debug=True)