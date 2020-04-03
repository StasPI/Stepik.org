#В какой-то момент в Институте биоинформатики биологи перестали понимать, что
#говорят информатики: они говорили каким-то странным набором звуков.
#В какой-то момент один из биологов раскрыл секрет информатиков: они
#использовали при общении подстановочный шифр, т.е.  заменяли каждый символ
#исходного сообщения на соответствующий ему другой символ.  Биологи раздобыли
#ключ к шифру и теперь нуждаются в помощи:
#Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
#Программа принимает на вход две строки одинаковой длины, на
#первой строке записаны символы исходного алфавита, на второй строке — символы
#конечного алфавита, после чего идёт строка, которую нужно
#зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#Пусть, например, на вход программе передано:
#abcd
#*d%#
#abacabadaba
##*%*d*%
#Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b
#заменяется на d, c — на % и d — на #.
#Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью
#этого шифра.  Получаем следующие строки, которые и передаём на
#вывод программы:
#*d*%*d*#*d*
#dacabac﻿
#Sample Input 1:
#abcd
#*d%#
#abacabadaba
##*%*d*%
#Sample Output 1:
#*d*%*d*#*d*
#dacabac
#Sample Input 2:
#dcba
#badc
#dcba
#badc
#Sample Output 2:
#badc
#dcba
start_list = []
job_list = []
code_dict = dict()
code_list = []
decode_list = []
#цикл ввода данных и загрузка строки по знакам как список - список в массив
for element in range(4):
    element = input()
    start_list = []
    for sign in element:
        start_list.append(sign)
    job_list.append(start_list)
job_list.append(start_list)
#цикл создания ключей шифрования сопоставлением элементов из 0 и 1 списоков где
#0 это ключ а 1 значение
for element in range(len(job_list[0])):
    code_dict[job_list[0][element]] = job_list[1][element]
#функция кодировки проверяет если буква есть ключ то записывает значение ключа
#и стоп, если такого ключа нет вообще тогда записывает букву
def foo_coder(element, code_dict):
    for key in code_dict:
        if element == key:
            code_list.append(code_dict[key])
            return
    if element != key:
        code_list.append(element)
#аналогичная функция но декодировки но сравниваем букву* с значением ключа, а
#записываем ключ
def foo_decoder(element, code_dict):
    for key in code_dict:
        if element == code_dict[key]:
            decode_list.append(key)
            return
    if element != code_dict[key]:
        decode_list.append(element)
#запуск функций
for element in job_list[2]:
    foo_coder(element, code_dict)
for element in job_list[3]:
    foo_decoder(element, code_dict)
#вывод
print(*code_list, sep = '')
print(*decode_list, sep = '')