from bs4 import BeautifulSoup
import requests

url = 'https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&name=%D0%A1%D0%BE%D1%87%D0%B8'
#      https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&name=%D0%A1%D0%BE%D1%87%D0%B8&PAGEN_1=2
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(page.text, 'html.parser')

print(soup)

hotels = soup.find_all('div', class_='result-item reestr-item')

with open('sources_govres_1.txt', 'w') as file:
    for hotel in hotels:
        # file.write(hotel.get('data-link'))
        print(hotel)