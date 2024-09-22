from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

# Инициализация драйвера браузера (здесь используется Chrome)
options = Options()
service = Service()

driver = webdriver.Chrome(options=options, service=service)

time.sleep(2)

# Загрузка страницы
url = 'https://maikop.spravker.ru/gostinicy/'
driver.get(url)
time.sleep(5)
# Получение HTML-кода страницы после загрузки всех динамических элементов
html_code = driver.page_source

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Находим ссылку на сайт гостиницы
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
        site = hotel.find('a')
        site_list.append(site.get('href'))
    except:
        site_list.append('-----')

#for item in hotels:
#    print(item)
#    print()

print(name_list, address_list, phone_list, site_list)

# Закрываем браузер
driver.quit()