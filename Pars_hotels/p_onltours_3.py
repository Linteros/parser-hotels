from bs4 import BeautifulSoup
import requests
import pandas as pd

links = []
names = []
rooms_list = []
addresses = []
dates = []

with open('sourses_ontrs_1.txt') as file:
    x = 0
    while x < 5:
        x += 1
        line = file.readline()
        url = line.strip()
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        element = soup.find('div', class_='pagetitle')
        name = element.find('h1').text
        print(name)
        address = element.find('div', class_='addr')
        address = ' '.join([address.find('span', { 'itemprop' : 'streetAddress'}).text,
                            address.find('span', { 'itemprop' : 'addressLocality'}).text,
                            address.find('span', { 'itemprop' : 'addressCountry'}).text])
        print(address)
        rooms = soup.find('div', class_='rooms roomsDefault')
        count = 0
        print(rooms)
        if rooms:
            for room in rooms:
                # res = room.find('div', class_='room-int room-description')
                res = room.find('ul', class_='room-data')
                res = res.rfind('span', class_='b').text
                if int(res):
                    count += int(res)
        print(count)
        links.append(url)
        names.append(name)
        addresses.append(address)
        rooms_list.append(count)

dates.append(pd.DataFrame({'Название':names,
'Адрес': addresses,
'Кол-во номеров':rooms_list,
'Сайт':links}))

dates = pd.concat(dates)

dates.to_excel(r"onltours.xlsx", index=False)