# -*- coding: utf-8 -*-
"""
Reverse API
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_page():
    return "Welcome to reverse sentence API!"

@app.route("/<text>")
def do_the_job(text):
    reversed_order = ' '.join(reversed(text.split()))
    return reversed_order

if __name__ == '__main__':
    app.run(debug=True)