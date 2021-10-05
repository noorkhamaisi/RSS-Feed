# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:39:34 2021

@author: get-a
"""


import requests
from bs4 import BeautifulSoup
import pandas as pd

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   print('hhhhhhh')
   return render_template("index.html")

        
        
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8086)