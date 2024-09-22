from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
service = Service()

driver = webdriver.Chrome(options=options, service=service)

names = []
addresses = []
phones = []
emails = []
links = []
rooms = []

with open('sources_govres_1.txt') as file:
    x = 0
    # for line in file.readlines():
    while x < 1:
        x += 1
        line = file.readline()
        url = line.strip()
        driver.get(url)
        driver.implicitly_wait(10)

        block = driver.find_element(By.CLASS_NAME, 'card-info-item')
        desc = block.find_elements(By.CLASS_NAME, 'info-part')

        n_flag = False
        a_flag = False
        p_flag = False
        e_flag = False
        l_flag = False

        for item in desc:
            # print(item.find('p', class_='info__name').text)
            if item.find_element(By.CLASS_NAME, 'info__name').text == 'Сокращенное наименование':
                names.append(item.find_element(By.CLASS_NAME, 'info__text').text)
                n_flag = True
            elif item.find_element(By.CLASS_NAME, 'info__name').text == 'Адрес':
                addresses.append(item.find_element(By.CLASS_NAME, 'info__text').text)
                a_flag = True
            elif item.find_element(By.CLASS_NAME, 'info__name').text == 'Телефон':
                phones.append(item.find_element(By.CLASS_NAME, 'info__text').text)
                p_flag = True
            elif item.find_element(By.CLASS_NAME, 'info__name').text == 'Email':
                emails.append(item.find_element(By.CLASS_NAME, 'info__text link').text)
                e_flag = True
            elif item.find_element(By.CLASS_NAME, 'info__name').text == 'Сайт':
                links.append(item.find_element(By.CLASS_NAME, 'info__text link').text)
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
        
        #count = 0
        #room = soup.find('table', class_='numbers-table card-info-item__table').find_all('tr')
        #for qnt in room:
        #    count += int(qnt.find('td', class_='numbers-quantity').text)
        #rooms.append(count)

print(names)
print(phones)
print(emails)
print(addresses)
print(links)
print(rooms)

driver.quit()