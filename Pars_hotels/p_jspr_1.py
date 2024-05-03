from bs4 import BeautifulSoup
import requests
import re

# Define URL
url = 'https://maikop.spravker.ru/gostinicy/'

pages = requests.get(url)

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text, 'lxml')

hotels = soup.find_all('div', class_= 'org-widget__in')

name_list = []
address_list = []
phone_list = []
site_list = []

for hotel in hotels:
    name_list.append(hotel.find('h3', class_ = 'org-widget-header__title').text.strip())
    address_list.append(hotel.find('span', class_ = 'org-widget-header__meta org-widget-header__meta--location').text.strip())
    
    try:
        phone_list.append(hotel.find('dd', class_ = 'spec__value').text.strip())
    except:
        phone_list.append('-----')

    try:
        site = hotel.find('span', class_ = 'js-pseudo-link').text.strip()
        site_list.append('Есть сайт')
    except:
        site_list.append('-----')

import pandas as pd

dates = pd.DataFrame({'Name':name_list,
 'Address': address_list,
 'Phone':phone_list,
 'Site':site_list})

dates1 = pd.DataFrame({'Name':name_list,
 'Address': address_list,
 'Phone':phone_list,
 'Site':site_list})

print(pd.concat([dates, dates1]))

# dates.to_excel(r"pars.xlsx", index=False)

print(dates)