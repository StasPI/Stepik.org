# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# Конкретный пример ввода-вывода приведён ниже.
# Порядок вывода команд произвольный.
# Sample Input:
# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# Sample Output:
# Зенит:2 2 0 0 6
# ЦСКА:2 0 1 1 1
# Спартак:2 0 1 1 1

first_list = []
first_set = set()
count = 0
number_rows = int(input())
# запуск цикла получения данных по количеству строк введенному ранее + разбивка на элементы по знаку и погрузка в список
for line in range(number_rows):
    line = input().split(';')
    first_list.append(line)
    count = 0
    first_dict = {}
# вложенный цикл который загружает в множество исключительно названия команд
    for j in range(int(len(line) / 2)):
        first_set.add(line[count])
        count += 2
# функция которая считает количество победа\ничья\поражение и т.д. путем ряда вложенных циклов которые осуществляют
# проверку входит ли команда из множества в элемент вложенного списка и если да то проверяет по различных условиям
# ее вхождения определяя позицию и добавляя в счетчик при соответствии определенным условиям


def foo_sh(set_element, first_list):
    count_inter = 0
    count_win = 0
    count_draw = 0
    count_defeat = 0
    total_points = 0
    win = 3
    draw = 1
    for list_element in first_list:
        for element in list_element:
            if element == set_element:
                count_inter += 1
                if list_element.index(set_element) == 0:
                    if list_element[1] > list_element[3]:
                        count_win += 1
                    elif list_element[1] == list_element[3]:
                        count_draw += 1
                    else:
                        count_defeat += 1
                elif list_element.index(set_element) == 2:
                    if list_element[3] > list_element[1]:
                        count_win += 1
                    elif list_element[3] == list_element[1]:
                        count_draw += 1
                    else:
                        count_defeat += 1
    total_points = (count_win * win + count_draw * draw)
    print(set_element + ':' + str(count_inter) + ' ' + str(count_win) + ' ' +
          str(count_draw) + ' ' + str(count_defeat) + ' ' + str(total_points))


# запуск функции с одним значением из множества и полным списком
for set_element in first_set:
    foo_sh(set_element, first_list)
