'''
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго
с 2001 года по настоящее время.
Одним из атрибутов преступления является его тип – Primary Type.
Вам необходимо узнать тип преступления, которое было зафиксировано максимальное 
число раз в 2015 году.
Файл с данными:
Crimes.csv
'''

import csv
import re
from collections import Counter

Primary_Type = []

# через регулярку
with open(r'A:\Crimes.csv') as r:
    reader = csv.reader(r)
    for row in reader:
        result = re.findall(r'\d{2}\/\d{2}\/2015', str(row))
        if result:
            Primary_Type.append(row[5])

# #через поиск в элементе списка
# with open(r'A:\Crimes.csv') as r:
#     reader = csv.reader(r)
#     for row in reader:
#         if '2015' in row[2]:
#             Primary_Type.append(row[5])

print(Counter(Primary_Type).most_common(1))
