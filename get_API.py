# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:37:28 2018
Get_Print_string_API
@author: moazm
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Please Enter any string'
@app.route('/<text>')
def print_string(text):
    return text
if __name__ == '__main__':
    app.run(debug=True)