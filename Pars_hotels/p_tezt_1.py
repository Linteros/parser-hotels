from bs4 import BeautifulSoup
import requests

url = 'https://tez-travel.com/countries/russia/resorts/tuapse/hotels/'

pages = requests.get(url)

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text, 'html.parser')

cats = soup.find_all('ul', class_='grid-row list list__3column')

with open('sources_tezt_2.txt', 'w') as file:
    for cat in cats:
        hotels = cat.find_all('li', class_='holiday-list__item')
        for hotel in hotels:
            file.write(hotel.find('a').get('href') + '\n')