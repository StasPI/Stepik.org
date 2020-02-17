start_list = []
job_list = []
final_list = []
job_set = set()
job_dict = dict()
key_number = 0
finish_str = ()
#открываю файл, читаю, перебираю элементы как строку убирая пробелы, переводя в нижний регист,
# деля на элементы, записываю в список(получается по строчно список в списке).
with open(r'A:\a.txt') as inf:
    for line in inf:
        line = line.strip().lower().split()
        start_list.append(line)
#перебором копирую элементы из первого списка в рабочий списокок по что бы избежать вложенности.
for i in start_list:
    for j in i:
        job_list.append(j)
#заполняю рабочее множество что бы убрать дубликаты затем перевожу значения в новый список
for list_element in job_list:
    job_set.add(list_element)
for set_element in job_set:
    final_list.append(set_element)
#сортирую списки и переворачиваю их(по условиям задачи в вывод должно попасть значение не только
#с максимальным количеством совпадений но и по альфавиту стоящая вначале(если количество одинаково)
job_list.sort()
job_list.reverse()
final_list.sort()
final_list.reverse()
#функция считает количество вхождений элемента и загружает в словарь 
#количество вхождений как ключ и элемент как его значение тем самым 
#перезаписывая по ключу элементы в обратном альфовидному порядке
def foo_count(element, job_list):
    count = 0
    for list_element in job_list:
        if list_element == element:
            count += 1
    job_dict[count] = element
#запускает функцию передавая ей элемент из списка без повторений и сразу целый список с повторениями 
#что бы пройтись каждым значением по всему списку и найти количество вхождений элемента
for element in final_list:
    foo_count(element, job_list)
#цикл удаляет по ключу все вхождения начиная от единицы до тех пор пока в словаре
# не остается одной записи где ключ то есть число вхождений максимально
while len(job_dict) > 1:
    key_number += 1
    if key_number in job_dict:
        del job_dict[key_number]
#для последующего вызова добирает значения счетчика ключа до соответствия максимальному ключу 
#по средствам того что функция работает пока значение не равно ключу из словаря
while not job_dict.get(key_number):
    key_number += 1
#загружаю в строку сначала значение по ключу, затем добавляю пробел, затем вставляю номер ключа(переведя его в строку)
finish_str = job_dict.get(key_number)
finish_str += ' '
finish_str += str(key_number)
#готовую строку записываю в файл
with open(r'A:\b.txt', 'r+') as ouf:
    ouf.write(finish_str)

#Недавно мы считали для каждого слова количество его вхождений в строку. Но на все слова может быть не так 
#интересно смотреть, как, например, на наиболее часто используемые.
#Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит 
#самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько,
#вывести лексикографически первое (можно использовать оператор < для строк).
#В качестве ответа укажите вывод программы, а не саму программу.
#Слова, написанные в разных регистрах, считаются одинаковыми.
#Sample Input:
#abc a bCd bC AbC BC BCD bcd ABC
#Sample Output:
#abc 3