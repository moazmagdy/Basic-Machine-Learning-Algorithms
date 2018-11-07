# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 19:32:41 2018

@author: moazm
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Please Enter the length/width'
@app.route('/<int:length>/<int:width>')
def area(length, width):
    return 'The rectangle area = ' + str(length * width)

if __name__ == '__main__':
    app.run(debug=True)