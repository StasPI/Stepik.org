'''
Вася решил открыть АЗС (заправку). Чтобы оценить уровень конкуренции он хочет изучить количество заправок в 
интересующем его районе. Вася скачал интересующий его кусок карты 
OSM https://stepik.org/media/attachments/lesson/245681/map2.osm и хочет посчитать, сколько на нём отмечено 
точечных объектов (node), являющихся заправкой. В качестве ответа вам необходимо вывести одно число - 
количество АЗС.
"Как обозначается заправка в OpenStreetMap" - пример хорошего запроса чтобы узнать, как обозначается заправка
 в OpenStreetMap.
'''


import xmltodict
from requests import get

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
file_name = url[url.rindex('/') + 1:]
file_dir = 'A:\\task\\'
file_path = file_dir + file_name

with open(file_path, 'wb') as inf:
    inf.write(get(url).content)

with open(file_path, 'r', encoding='utf-8') as inf:
    text = inf.read()

dct = xmltodict.parse(text)

count = 0

for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if '@k' in tags and tags['@v'] == 'fuel':
            count += 1
        if isinstance(tags, list):
            for tag in tags:
                if '@k' in tag and tag['@v'] == 'fuel':
                    count += 1

print(count)
