from bs4 import BeautifulSoup
import requests
import pandas as pd

links = []
names = []
rooms = []
contacts = []
dates = []

with open('sources_tezt_2.txt') as file:
    for line in file.readlines():
        url = line.strip()
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        name = soup.find('h1', class_='h2 inner__h2').text
        names.append(name)
        address = 'None'
        desc = soup.find('ul', class_='hotel-desc-list')
        count = 0
        flag_link = False
        flag_cont = False
        flag_tel = False
        if desc:
            for item in desc:
                res = item.text.strip()
                if 'Сайт отеля: ' in res:
                    link = res[res.find(':') +2:]
                    links.append(link)
                    flag_link = True
                elif 'Телефон: ' in res:
                    contact = res[res.find(':') +2:]
                    flag_cont = True
                    flag_tel = True
                elif 'Email: ' in res and flag_tel:
                    contact += ';  \n' + res[res.find(':') +2:]
                elif 'Email: ' in res and not flag_tel:
                    contact = res[res.find(':') +2:]
                    flag_cont = True
                elif 'Количество номеров: ' in res:
                    count = int(res[res.find(':') +2:])
            
            rooms.append(count)
            if not flag_link:
                links.append('-----')
            if not flag_cont:
                contacts.append('-----')
            else:
                contacts.append(contact)
        else:
            rooms.append(count)
            links.append('-----')
            contacts.append('-----')

# print(len(names))
# print(len(contacts))
# print(len(rooms))
# print(len(links))

dates.append(pd.DataFrame({'Название':names,
'Контакты': contacts,
'Кол-во номеров':rooms,
'Сайт':links}))

dates = pd.concat(dates)

dates.to_excel(r"tezt_tyapse.xlsx", index=False)