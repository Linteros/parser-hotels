from bs4 import BeautifulSoup
import requests

# Define URL
url = 'https://majkop.jsprav.ru/gostinitsyi/'

pages = requests.get(url)

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text, 'lxml')

a_start = soup.header.div

# print(a_start)

names = soup.find_all('span', class_ = 'company-info-name-org')
addresses = soup.find_all('address', class_ = 'company-info-address-full company-info-text')
phones = soup.find_all('span', class_ = 'company-info-phone-number')
sites = soup.find_all('a', class_ = 'flex-r company-info-btn company-info-text company-info-site-open')

# print(sites[1].text)

name_list = []
address_list = []
phone_list = []
site_list = []

for i in names:
    name_list.append(i.text)

for i in addresses:
    address_list.append(i.text)

for i in phones:
    phone_list.append(i.text)

while len(phone_list) < len(name_list):
    phone_list.append('---')

for i in sites:
    site_list.append(i.text)

while len(site_list) < len(name_list):
    site_list.append('---')

# print(len(name_list), len(address_list), len(phone_list), len(site_list))

import pandas as pd

dates = pd.DataFrame({'Name':name_list,
 'Address': address_list,
 'Phone':phone_list,
 'Site':site_list})

print(dates)