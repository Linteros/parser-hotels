import requests
from bs4 import BeautifulSoup
import pandas as pd

dates = []
names = []
addresses = []
phones = []
emails = []
links = []
gov_links = []
rooms = []

with open('sources_govres_1.txt') as file:

    for line in file.readlines():
    
        # URL страницы
        url = line.strip()
        gov_links.append(url)
        # Заголовки для запроса
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
        # Запрос к странице с заголовками
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        block = soup.find('div', class_='card-info-item')
        if block:
            desc = block.find_all('div', class_='info-part')

        n_flag = False
        a_flag = False
        p_flag = False
        e_flag = False
        l_flag = False

        if desc:

            for item in desc:
                if item.find('p', class_='info__name').text == 'Сокращенное наименование':
                    names.append(item.find('p', class_='info__text').text)
                    n_flag = True
                elif item.find('p', class_='info__name').text == 'Адрес':
                    addresses.append(item.find('p', class_='info__text').text)
                    a_flag = True
                elif item.find('p', class_='info__name').text == 'Телефон':
                    phones.append(item.find('p', class_='info__text').text)
                    p_flag = True
                elif item.find('p', class_='info__name').text == 'Email':
                    emails.append(item.find('a', class_='info__text link').text)
                    e_flag = True
                elif item.find('p', class_='info__name').text == 'Сайт':
                    links.append(item.find('a', class_='info__text link').text)
                    l_flag = True

        if not n_flag:
            names.append('-----')
        if not a_flag:
            addresses.append('-----')
        if not p_flag:
            phones.append('-----')
        if not e_flag:
            emails.append('-----')
        if not l_flag:
            links.append('-----')
        
        count = 0
        
        table = soup.find('table', class_='numbers-table card-info-item__table')
        if table:
            room = table.find_all('td')
        if room:
            for qnt in room:
                if qnt.get('class') == ['numbers-quantity']:
                    count += int(qnt.text)
        rooms.append(count)

dates.append(pd.DataFrame({'Название':names,
'Адрес': addresses,
'Телефон': phones,
'Email': emails,
'Кол-во номеров':rooms,
'Сайт':links,
'Реестр': gov_links}))

dates = pd.concat(dates)

dates.to_excel(r"govres_sochi.xlsx", index=False)