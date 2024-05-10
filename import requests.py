import requests
from bs4 import BeautifulSoup
from datetime import date, datetime
import csv

title = ''
url = 'https://books.toscrape.com/catalogue/page-1.html'.format(title)

headers ={
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
  }

page_pos = 0
df = []

# for page in range(1,3):
print('scrapping page:')
req_web = requests.get(url)
soup = BeautifulSoup(req_web.text, 'html.parser')
buku = soup.findAll('article', class_='product_pod')
# title =soup.find_all('a', attrs={'title': True})
# print(soup.prettify())

for i in buku:
  title = i.h3.a['title']
  price = i.find('p', class_='price_color').get_text().replace('Â','')
  rating = i.p['class'][1]
  pic = i.img['src']
  print(title)
  print(price)
  print(rating+' stars')
  print(pic)
  df.append([title,price,rating,pic])
column = ['title','price','rating','pic']
today = date.today()
file = csv.writer(open('scrap_book.csv'.format(today), 'w',newline=''))
file.writerow(column)
for x in df:
  file.writerow(x)
    
