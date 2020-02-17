'''
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, 
составив справочник продуктов с указанием калорийности на 100 грамм, а также содержание белков, 
жиров и углеводов на 100 грамм продукта. Ему не удалось найти всю информацию, поэтому некоторые 
чейки остались незаполненными (можно считать их значение равным нулю). Также он использовал 
какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой. Таблица 
доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx
Вася составил раскладку по продуктам на весь поход (она на листе "Раскладка") с указанием 
номера дня, названия продукта и его количества в граммах. Для каждого дня посчитайте 4 числа: 
суммарную калорийность и граммы белков, жиров и углеводов. Числа округлите до целых вниз и 
введите через пробел. Информация о каждом дне должна выводиться в отдельной строке.
'''
import xlrd
from math import floor

product_value = {}
cheklist = []
otvet = [0, 0, 0, 0]

rb = xlrd.open_workbook('A:\\trekking3.xlsx')


def table(index, table, form):
    sheet = rb.sheet_by_index(index)
    row_vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    table_value(row_vals, table, form)


def table_value(row_vals, table, form):
    if form == 'Dict':
        for row in row_vals:
            table[row[0]] = row[1:]
    elif form == 'List':
        for row in row_vals:
            table.append(row)


table(0, product_value, 'Dict')
table(1, cheklist, 'List')

for product in product_value:
    for element in product_value[product]:
        if element == '':
            product_value[product][product_value[product].index(element)] = 0

days = int(cheklist[-1][0])

for day in range(days):
    for product in cheklist[1:]:
        if day + 1 == int(product[0]):
            otvet[0] += float(product_value[product[1]][0]) / \
                100 * float(product[2])
            otvet[1] += float(product_value[product[1]][1]) / \
                100 * float(product[2])
            otvet[2] += float(product_value[product[1]][2]) / \
                100 * float(product[2])
            otvet[3] += float(product_value[product[1]][3]) / \
                100 * float(product[2])
    print(*list(map(floor, otvet)))
    otvet = [0, 0, 0, 0]
