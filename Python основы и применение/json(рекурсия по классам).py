'''
Вам дано описание наследования классов в формате JSON. 
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого 
JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список 
имен прямых предков.
Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Эквивалент на Python:
class A:
    pass
class B(A, C):
    pass
class C(A):
    pass
Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не 
наследуется явно от одного класса более одного раза.
Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в 
следующем формате.
<имя класса> : <количество потомков>
Выводить классы следует в лексикографическом порядке.
Sample Input:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:
A : 3
B : 1
C : 2
'''

import json

json_str = json.loads(input())
classes_set = set()
check_set = set()

for name_class in json_str:
    classes_set.add(name_class['name'])
    for parent in name_class['parents']:
        classes_set.add(parent)

classes_list = list(classes_set)
classes_list.sort()


def search1(element_name):
    for element in json_str:
        if element['name'] not in check_set:
            if check_set.intersection(element['parents']):
                check_set.add(element['name'])
                for element_name in element['parents']:
                    search1(element_name)


def search(name_class):
    for element in json_str:
        if name_class in element['parents']:
            check_set.add(element['name'])
            search1(element['name'])
    print(name_class, ':', len(check_set) + 1)


for name_class in classes_list:
    check_set.clear()
    search(name_class)
