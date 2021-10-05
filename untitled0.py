#import library
import requests
from bs4 import BeautifulSoup
import pandas as pd
#enter URL
url = "http://www.ynet.co.il/Integration/StoryRss2.xml"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")


#print(soup.prettify())


items = soup.findAll('item')

news_items = []
for item in items:
    news_item = {}
    news_item['title'] = item.title.text
    news_item['description'] = item.description.text
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
   # print(news_item)
   # break
    
    
    
df = pd.DataFrame(news_items,columns=['title','description','link','pubDate'])
df.head()
df.to_csv('BBCdata1.csv',index=False, encoding = 'utf-8')

a = pd.read_csv("BBCdata1.csv", encoding = 'utf-8')

a.to_html("Tableeee.html")

