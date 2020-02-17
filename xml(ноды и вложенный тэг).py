'''
В OpenStreetMap XML встречаются теги node, которые соответствуют некоторым точкам на карте. 
Ноды могут не только обозначать какой-то точечный объект, но и входить в состав way (некоторой линии, 
возможно замкнутой) и не иметь собственных тегов. Для доступного по ссылке 
https://stepik.org/media/attachments/lesson/245678/map1.osm фрагмента карты посчитайте, сколько node 
имеет хотя бы один вложенный тэг tag, а сколько - не имеют. В качестве ответа введите два числа, 
разделённых пробелом.
'''

import xmltodict
from requests import get


url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
file_name = url[url.rindex('/') + 1:]
file_dir = 'A:\\task\\'
file_path = file_dir + file_name

with open(file_path, 'wb') as inf:
    inf.write(get(url).content)

with open(file_path, 'r', encoding='utf-8') as inf:
    text = inf.read()

dct = xmltodict.parse(text)

count_node = 0
count_node_tag = 0
for node in dct['osm']['node']:
    count_node += 1
    if 'tag' in node:
        count_node_tag += 1

print(count_node_tag, count_node - count_node_tag)
