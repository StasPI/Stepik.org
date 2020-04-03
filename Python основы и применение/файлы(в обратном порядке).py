'''
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
Пример входного файла:
ab
c
dde
ff
﻿Пример выходного файла:
ff
dde
c
ab
'''
with open('A:\\dataset_24465_4.txt') as f, open('A:\\a.txt', 'w') as w:
    l_revers = []
    for line in f:
        l_revers.append(line.rstrip())
    for line in l_revers[::-1]:
        w.write(str(line) + '\n')