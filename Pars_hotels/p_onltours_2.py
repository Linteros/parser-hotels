from bs4 import BeautifulSoup
import requests

url = 'https://sochi.vashotel.ru/?searchID=hotel_type_1%3D1%3Bhotel_type_4%3D1%3Bhotel_type_5%3D1%3Bhotel_type_6%3D1%3Bhotel_type_7%3D1%3Bhotel_type_9%3D1'

pages = requests.get(url)

# parser-lxml = Change html to Python friendly format
soup = BeautifulSoup(pages.text, 'html.parser')

hotels = soup.find_all('a', class_= 'hotel-link mapObject')

with open('sourses_ontrs_1.txt', 'w') as file:
    for link in hotels:
        file.write(link.get('href') + '\n')

with open('sourses_ontrs_1.txt', 'a') as file:
    for i in range(2, 210):
        url = 'https://sochi.vashotel.ru/page' + str(i) + '?searchID=hotel_type_1%3D1%3Bhotel_type_4%3D1%3Bhotel_type_5%3D1%3Bhotel_type_6%3D1%3Bhotel_type_7%3D1%3Bhotel_type_9%3D1'
        pages = requests.get(url)
        soup = BeautifulSoup(pages.text, 'html.parser')
        hotels = soup.find_all('a', class_= 'hotel-link mapObject')
        for link in hotels:
            file.write(link.get('href') + '\n')