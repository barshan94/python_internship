# -*- coding: utf-8 -*-
"""DS1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jeF79vRxUDt8zxEZo_YmVF20ITbpcJEQ
"""

#DATA SCIENCE

#WEB SCRAPING - BEAUTIFUL SOUP
#url : https://www.amazon.in/Samsung-Phantom-Storage-Additional-Exchange/product-reviews/B09SH994JW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews

import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.in/Samsung-Phantom-Storage-Additional-Exchange/product-reviews/B09SH994JW/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = requests.get(url)
page #<Response [200]> is okay, but <Response [503]> is an error - try rerunning your cell until you get <Response [200]>
#Even after trying multiple times ,if <Response [200]> is not printed , check your url

#ALWAYS IGNORE TOP POSITIVE and TOP CRITICAL REVIEWS
#WE all know that there are 10 reviews in the Customer Review Page

page.content
#Here we have got the source code of the Amazon Customer Review Page
#But the source is jumbled and not in readable format

soup = bs(page.content,'html.parser')
#html.parser converts the html code into better readable format
soup

#Now let us condiser the Review Names
names = soup.find_all('span',class_ = 'a-profile-name')[2:]
names

len(names)

#Now let us create a dataframe using the data from the names list
import pandas as pd
df = pd.DataFrame(names,columns = {'Customer Name'})
df

#Next is review title
r_title = soup.find_all('a',class_ = 'review-title')
r_title

len(r_title)

#Data Cleaning or Data Filtering
review_title = [] #empty list
#for i in range(0,10):
for i in range(0,len(r_title)):
  review_title.append(r_title[i].get_text()[1:-1])
review_title

#Next is review date
dates = soup.find_all('span',class_ = 'review-date')[2:]
dates

len(dates)

#Data Cleaning
review_date = [] #empty list
for i in range(0,len(dates)):
  review_date.append(dates[i].get_text().replace('Reviewed in India 🇮🇳 on ',''))
review_date

df['Review title'] = review_title
df['Review dates'] = review_date
df

#Review Content
#Review Rating in stars