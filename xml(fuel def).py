'''
Вася, открывший заправку в прошлом уроке, разорился. Конкуренция оказалась слишком большой. Вася предполагает, 
что это произошло от того, что теги заправки могут быть не только на точке, но и на каком-то контуре. Определите, 
сколько заправок на самом деле (не только обозначенных точкой) есть на фрагменте карты 
https://stepik.org/media/attachments/lesson/245681/map2.osm
'''

import xmltodict
import urllib.request

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
file_dir = 'A:\\task\\'
file_name = url[url.rindex('/') + 1:]
file_path = file_dir + file_name
urllib.request.urlretrieve(url, file_path)

with open(file_path, 'r', encoding='utf-') as inf:
    text = inf.read()

dct = xmltodict.parse(text)


def screan(core_element, value):
    count = 0
    for node in dct['osm'][core_element]:
        if 'tag' in node:
            tags = node['tag']
            if '@k' in tags and tags['@v'] == value:
                count += 1
            if isinstance(tags, list):
                for tag in tags:
                    if '@k' in tag and tag['@v'] == value:
                        count += 1
    return count


a = screan('node', 'fuel')
b = screan('way', 'fuel')

print(a+b)
