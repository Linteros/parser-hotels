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

# Загрузка страницы
# всего 209 страниц
url = 'https://sochi.vashotel.ru/joy-apartments'
driver.get(url)
driver.implicitly_wait(10)
# class of each element on page: found-hotel
# class of link: hotel-link mapObject
# elements = driver.find_elements(By.CLASS_NAME, 'room-data')

# [print(i) for i in elements]

driver.quit()