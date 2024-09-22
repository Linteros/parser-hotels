from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера браузера
options = Options()
service = Service()

driver = webdriver.Chrome(options=options, service=service)

time.sleep(2)

url = 'https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/?set_filter=y&name=%D0%A1%D0%BE%D1%87%D0%B8'
driver.get(url)
driver.implicitly_wait(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

hotels = soup.find_all('div', class_='result-item reestr-item')

with open('sources_govres_1.txt', 'w') as file:
    for hotel in hotels:
        file.write('https://tourism.gov.ru' + hotel.get('data-link') + '\n')