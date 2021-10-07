#import library
import requests
from bs4 import BeautifulSoup
import pandas as pd
from pretty_html_table import build_table
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

df.to_csv('BBCdata1.csv',index=True, encoding = 'utf-8')

a = pd.read_csv("BBCdata1.csv", encoding = 'utf-8')

a.to_html("Tableeee.html")


df = pd.read_csv('BBCdata1.csv', encoding = 'utf-8')
#html_table_blue_light = build_table(df, 'blue_light')

html_table_blue_light = build_table(df, 'yellow_dark', font_size='medium'
                        , font_family='Open Sans, sans-serif'
                        , text_align='left'
                        , width='auto'
                        , index=False
			, even_color='black'
			, even_bg_color='white'
                        )

# Save to html file
with open('pretty_table.html', 'w', encoding = 'utf-8') as f:
    f.write(html_table_blue_light)
  