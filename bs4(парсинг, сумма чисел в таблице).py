'''
В файле https://stepik.org/media/attachments/lesson/209723/3.html находится одна таблица. 
Просуммируйте все числа в ней и введите в качестве ответа одно число - эту сумму. Для доступа 
к ячейкам используйте возможности BeautifulSoup.
'''

import requests
from bs4 import BeautifulSoup

sum_list = []
req = requests.get(
    'https://stepik.org/media/attachments/lesson/209723/3.html')
req = req.content

soup = BeautifulSoup(req, 'html.parser')

for number in soup.find_all('td'):
    sum_list.append(int(number.get_text()))

print(sum(sum_list))
