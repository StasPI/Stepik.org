'''
В этой задаче нужно просто установить библиотеку xmltodict, скачать файл 
https://stepik.org/media/attachments/lesson/245571/map1.osm, создать в директории с файлом скрипт со 
следующим содержанием:
import xmltodict
fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()
parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
и ввести в качестве ответа вывод этого скрипта.
'''

import xmltodict

from requests import get


url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
file_start_dir = 'A:\\task\\'
file_name = url[url.rindex('/') + 1:]
file_dir = file_start_dir + file_name

with open(file_dir, 'wb') as inf:
    inf.write(get(url).content)

fin = open(file_dir, 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml['osm']['node'][100]['@id'])
