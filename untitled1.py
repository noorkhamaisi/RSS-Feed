#import library
import requests
from bs4 import BeautifulSoup
import pandas as pd

import os
import os.path

#from IPython.display import HTML
#enter URL
url = "http://www.ynet.co.il/Integration/StoryRss2.xml"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

path = os.getcwd() #Gets the current working directory

#print(os.chdir("..")) #Go up one directory from working directory

#soup.prettify()

#print (soup)
items = soup.findAll('item')

print("hhhhhhhhhhhhhhhhhh")

print(items[0])

print("--------------------")



print("--------------------")
print(items[0].description)

print("--------------------")
print(items[0].title)

print("--------------------")
print(items[0].link)

print("--------------------")
print(items[0].pubDate)

news_items = []
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
  #  print(news_item)
   # break
    
    
    
df = pd.DataFrame(news_items,columns=['title','description','link','pubDate'])



html = df.to_html()

print("--------------------------------------------------------")
print(html)

text_file = open(path+"\\"+"templates"+"\\"+"index.html", "w", encoding='utf-8')
text_file.write(html)
text_file.close()