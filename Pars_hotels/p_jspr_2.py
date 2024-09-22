from bs4 import BeautifulSoup
import requests
import pandas as pd

# Define URL
urls = ['https://maikop.spravker.ru/gostinicy/',
        'https://maikop.spravker.ru/gostinicy/?page=2',
        'https://maikop.spravker.ru/gostinicy/?page=3',
        'https://maikop.spravker.ru/gostinicy/?page=4']

dates = []

for url in urls:

    pages = requests.get(url)

    # parser-lxml = Change html to Python friendly format
    soup = BeautifulSoup(pages.text, 'html.parser')

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

    dates.append(pd.DataFrame({'Название':name_list,
'Адрес': address_list,
'Телефон(ы)':phone_list,
'Сайт':site_list}))

dates = pd.concat(dates)

dates.to_excel(r"spravker-maikop.xlsx", index=False)