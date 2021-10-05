# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:00:02 2021

@author: get-a
"""


# pip install -r reuirments.txt

from flask import Flask

import feedparser


app = Flask(__name__)

@app.route("/")
def showresults():
    NewsFeed = feedparser.parse("http://www.ynet.co.il/Integration/StoryRss2.xml")
    sumn=""
    print ('Number of RSS posts :', len(NewsFeed.entries))
    for i in range(1,len(NewsFeed.entries)):
        entry = NewsFeed.entries[i]
        print ('Post Title :',entry.title)
        sumn=sumn+"/n"+entry.title
        
    return sumn
        
        
        
        
        
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)