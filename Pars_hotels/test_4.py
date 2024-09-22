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
url = 'https://maikop.spravker.ru/gostinicy/'
driver.get(url)
time.sleep(5)

links = []
elements = driver.find_elements(By.CLASS_NAME, 'org-widget__spec')

for element in elements:
    try:
        link = element.find_element(By.CLASS_NAME, 'js-pseudo-link')
        link = link.find_element(By.TAG_NAME, 'a')
        links.append(link.text)
    except:
        links.append('-----')

print(links)

# Закрываем браузер
driver.quit()