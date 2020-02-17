'''
Вася планирует карьеру и переезд. Для это составил таблицу, в которой для каждого региона записал 
зарплаты для разных интересные ему профессий. Таблица доступна по ссылке 
https://stepik.org/media/attachments/lesson/245267/salaries.xlsx. Выведите название региона с самой 
высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после его 
упорядочивания) и, через пробел, название профессии с самой высокой средней зарплатой по всем регионам. 
'''

import xlrd
from statistics import median
start = {}
statistics = {}
rb = xlrd.open_workbook('A:\\salaries.xlsx')

# получаю два списка первый по строкам второй по столбцам
sheet = rb.sheet_by_index(0)
row_vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
col_vals = [sheet.col_values(colnum) for colnum in range(sheet.ncols)]


def start_dict(args):
    # подготавливаю словарь с данными
    for element in args:
        start[element[0]] = element[1:]
    del start['']


def statistics_dict(args):
    # создаю словарь с медианным значением
    for element in args:
        statistics[element] = median(args[element])
    start.clear()


def statistics_prof(args):
    # создаю словарь со средним значением
    for element in args:
        statistics[element] = sum(args[element]) / len(args[element])
    start.clear()


def result(args):
    # ищу максимальное значение, вывожу победителя
    value = 0
    for element in args:
        if args.get(element) >= value:
            value = args.get(element)
            reg = element
    print(reg, end=' ')
    statistics.clear()


start_dict(row_vals)
statistics_dict(start)
result(statistics)

start_dict(col_vals)
statistics_prof(start)
result(statistics)
