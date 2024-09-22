import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://tourism.gov.ru/reestry/reestr-gostinits-i-inykh-sredstv-razmeshcheniya/otel-ranovsky-park-ranovskiy-park-ip-mizerova-v-v/"

# Заголовки для запроса
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Запрос к странице с заголовками
response = requests.get(url, headers=headers)

# Проверка успешности запроса
if response.status_code == 200:
    # Парсинг HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлечение заголовка страницы
    title = soup.find('title').get_text()
    print(f"Title: {title}")

    # Извлечение основной информации
    main_info = soup.find('div', class_='main-info')
    if main_info:
        short_name = main_info.find(text='Сокращенное наименование').find_next('div').get_text(strip=True)
        address = main_info.find(text='Адрес').find_next('div').get_text(strip=True)
        phone = main_info.find(text='Телефон').find_next('div').get_text(strip=True)
        email = main_info.find(text='Email').find_next('div').get_text(strip=True)

        print(f"Сокращенное наименование: {short_name}")
        print(f"Адрес: {address}")
        print(f"Телефон: {phone}")
        print(f"Email: {email}")
    else:
        print("Основная информация не найдена на странице.")

    # Извлечение информации о номерах
    rooms_info = soup.find('div', class_='rooms-info')
    if rooms_info:
        room_count = rooms_info.find(text='Количество номеров').find_next('div').get_text(strip=True)
        print(f"Количество номеров: {room_count}")
    else:
        print("Информация о номерах не найдена на странице.")

else:
    print(f"Не удалось загрузить страницу. Статус код: {response.status_code}")