#import library
import requests
import os
import os.path
from bs4 import BeautifulSoup
import pandas as pd
from pretty_html_table import build_table
from flask import Flask, render_template
#enter URL
url = "http://www.ynet.co.il/Integration/StoryRss2.xml"

resp = requests.get(url)

soup = BeautifulSoup(resp.content, features="xml")

path = os.getcwd() #Gets the current working directory

#print(soup.prettify())


items = soup.findAll('item')
news_items = []
for item in items:
    news_item = {}
   
    news_item['title'] = item.title.text
   # news_item['description'] = item.description.text
   
    d=item.description.text.split()[25:]
    news_item['description']=" ".join(d)
    news_item['link'] = item.link.text
    news_item['pubDate'] = item.pubDate.text
    news_items.append(news_item)
   # print(news_item)
   # break
    
    
    
df = pd.DataFrame(news_items,columns=['title','description','link','pubDate'])

df.to_csv('data1.csv',index=False, encoding = 'utf-8')

a = pd.read_csv("data1.csv", encoding = 'utf-8')

a.to_html("Table.html")


df = pd.read_csv('BBCdata1.csv', encoding = 'utf-8')
#html_table_blue_light = build_table(df, 'blue_light')

html_table_blue_light = build_table(df, 'yellow_dark', font_size='medium'
                        , font_family='Open Sans, sans-serif'
                        , text_align='left'
                        , width='auto'
                        , index=True
			, even_color='black'
			, even_bg_color='white'
                        )

# Save to html file
with open(path+"\\"+"templates"+"\\"+'pretty_table.html', 'w', encoding = 'utf-8') as f:
    f.write(html_table_blue_light)
  
    
  
app = Flask(__name__)

@app.route('/')
def home():
   print('hhhhhhh')
   return render_template("pretty_table.html")



app.run(host="127.0.0.1", port=8086)
        
'''       
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8086)
    '''