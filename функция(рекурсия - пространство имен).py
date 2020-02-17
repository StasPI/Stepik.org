#чистый код
num_str = int(input())
scopes = {'global': {'funcs': [], 'vars': []}}

def add(scopes, current_namespace, value):
    if current_namespace not in scopes:
        scopes[current_namespace] = {}
        scopes[current_namespace]['vars'] = []
        scopes[current_namespace]['vars'].append(value)
    else:
        scopes[current_namespace]['vars'].append(value)

def create(scopes, current_namespace, parent_namespace):
    if current_namespace not in scopes:
        scopes[current_namespace] = {}
        scopes[current_namespace]['funcs'] = []
        scopes[current_namespace]['vars'] = []
        scopes[parent_namespace]['funcs'].append(current_namespace)
        scopes[current_namespace]['parent'] = parent_namespace
    else:
        scopes[current_namespace]['funcs'].append(current_namespace)
        scopes[parent_namespace]['funcs'].append(current_namespace)

def get(scopes, namespace, value):
    if value in scopes[namespace]['vars']:
        return namespace
    else:
        try:
            namespace = scopes[namespace]['parent']
        except KeyError:
            return None
        return get(scopes, namespace, value)

for element in range(num_str):
    element = input().split()
    if element[0] == 'create':
        create(scopes, element[1], element[2])
    elif element[0] == 'add':
        add(scopes, element[1], element[2])
    else:
        print(get(scopes, element[1], element[2]))

                                                                    #Задание
#Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать 
#поддержку создания пространств имен и добавление в них переменных.
#В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#Вашей программе на вход подаются следующие запросы:
#create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
#add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из пространства
#<namespace>, или None, если такого пространства не существует
#Рассмотрим набор запросов
#add global a
#create foo global
#add foo b
#create bar foo
#add bar a
#Структура пространств имен описанная данными запросами будет эквивалентна структуре пространств имен,
#созданной при выполнении данного кода
#a = 0
#def foo():
#  b = 1
#  def bar():
#    a = 2
#В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. 
#Далее мы объявляем функцию foo, что влечет за собой создание локального для нее пространства имен 
#внутри пространства global. В нашем случае, это описывается командой create foo global. Далее мы 
#объявляем внутри функции foo функцию bar, тем самым создавая пространство bar внутри пространства foo,
#и добавляем в bar переменную a.
#Добавим запросы get к нашим запросам
#get foo a
#get foo c
#get bar a
#get bar b
#Представим как это могло бы выглядеть в коде
#a = 0
#def foo():
#  b = 1
#  get(a)
#  get(c)
#  def bar():
#    a = 2
#    get(a)
#    get(b)
#Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
#Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена 
#переменная a, но в пространстве global, внутри которого находится пространство foo, она объявлена.
#Аналогично, результатом запроса get bar b будет являться foo, а результатом работы get bar a будет являться bar.
#Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве 
#global не была объявлена переменная с.
#Более формально, результатом работы get <namespace> <var> является
#<namespace>, если в пространстве <namespace> была объявлена переменная <var>
#get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>,
#если переменная не была объявлена
#None, если не существует <parent>, т. е. <namespace>﻿ – это global
#Формат входных данных
#В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
#В каждой из следующих n строк дано по одному запросу.
#Запросы выполняются в порядке, в котором они даны во входных данных.
#Имена пространства имен и имена переменных представляют из себя строки длины не более 10, состоящие из строчных
#латинских букв.
#Формат выходных данных
#Для каждого запроса get выведите в отдельной строке его результат.
#Sample Input:
#9
#add global a
#create foo global
#add foo b
#get foo a
#get foo c
#create bar foo
#add bar a
#get bar a
#get bar b
#Sample Output:
#global
#None
#bar
#foo


                                                        ##закомментированный донельзя...
##запрос на ввод количества строк
#num_str = int(input())
##создание словаря, глобальные ключ с вложенными значениями словарями функции и
##значения
#scopes = {'global': {'funcs': [], 'vars': []}}
##функция заполнения словаря, добаляет значение в опреденную область пространств
#def add(scopes, current_namespace, value):
##проверяет есть ли такое пространство имен в словаре и если его там нет
#    if current_namespace not in scopes:
##добавляет в словарь это пространство имен ввиде ключа с пустым значением
#        scopes[current_namespace] = {}
##создает ключ варианты и к нему значение пустой список в ранее созданном
##простве имен
#        scopes[current_namespace]['vars'] = []
##добавляет в варианты полученную переменную
#        scopes[current_namespace]['vars'].append(value)
##а если есть добаляет значение переменной в список переменных данного имени
##пространства
#    else:
#        scopes[current_namespace]['vars'].append(value)
##функция заполения словаря, создает функцию в определенной области пространства
##или подпространства имен
#def create(scopes, current_namespace, parent_namespace):
##проверяет что бы не было такой функции в словаре
#    if current_namespace not in scopes:
##создает словарь с ключом названием фукции в указанном пространстве с пустым
##значением
#        scopes[current_namespace] = {}
##создает в функции как значение словарь с ключем функция и значением в виде
##пустого списка
#        scopes[current_namespace]['funcs'] = []
##создает в функции как значение словарь с ключем значения и значением в виде
##пустого списка
#        scopes[current_namespace]['vars'] = []
##записывает название функции в виде значения словаря функции в родительское
##пространство имен
#        scopes[parent_namespace]['funcs'].append(current_namespace)
##записывает название родительского пространства имен в виде значения в
##создаваемый этим же действием ключ родитель список в по названию функции
#        scopes[current_namespace]['parent'] = parent_namespace
##если фунция повторяется
#    else:
##записывает название функции в виде значение словаря функции в список по
##названию функции
#        scopes[current_namespace]['funcs'].append(current_namespace)
###записывает название родительского пространства имен в виде значения в
###создаваемый этим же действием ключ родитель список в по названию функции
#        scopes[parent_namespace]['funcs'].append(current_namespace)
##функия запроса/поиска значения для функции из области вложенных пространств
##имен
#def get(scopes, namespace, value):
##проверяет входит ли полученное значение в словаре с переденным пространством
##имен в списке ключа варианты
#    if value in scopes[namespace]['vars']:
##если входит возвращает на выход название области видимости
#        return namespace
##в ином случае
#    else:
##принять как правду
#        try:
##простанство имен равное как пространство имен в родительском списке по ключу
##уже полученного списка пространств в словаре
#            namespace = scopes[namespace]['parent']
##в случае когда перебраны все варианты имен пространства будет ошибка в
##отсутствии ключа
#        except KeyError:
##это значит что искомой переменной в цепочки подпространств нету и на вывод
##подается нон.
#            return None
##возвращает то есть запускает рекурсию
#        return get(scopes, namespace, value)
##цикл запрашивает на ввод строки по количеству запрошенному ранее
#for element in range(num_str):
##запрос строки и получение элементов ввиде списка
#    element = input().split()
##если нулевой элемент это слово создать
#    if element[0] == 'create':
##то передает в функцию создать данные в виде словаря и первого(имя функции) и
##второго элемента(область пространства) из списка полученной строки
#        create(scopes, element[1], element[2])
##иначе если нулевой элемент это добавить
#    elif element[0] == 'add':
##то передает в функцию создать данные в виде словаря и первого(области
##пространства) и второго элемента(переменной) из списка полученной строки
#        add(scopes, element[1], element[2])
##в ином случае
#    else:
##публикует через поиск в функции с последующей передачей в функцию словаря,
##первого значения(имя функцит) второго значентя(имя переменной)
#        print(get(scopes, element[1], element[2]))


                                        ##не правильное - решение которое пройдет не все тесты
#command_list = []
#command_tuple = tuple()

#num_str = int(input())
#def f_input(num_str):
#    for num in range(num_str):
#        command_list.append(input().split())

#f_input(num_str)
#command_tuple = (command_list)
##del comman_list
#def foo(element):
#    if element[0] == 'get':
#        con_list = command_list[: command_list.index(element)]
#        for el in con_list[::-1]:
#            if el[0] != 'get':
#                if element[2] == el[2]:
#                    print(el[1])
#                    return
#                else:
#                    if con_list.index(el) == 0:
#                        print('None')
#                        return

#for element in command_list:
#    foo(element)

                                                                #один из тестов
#Test6
#11
#create foo global
#create bar foo
#create barz bar
#create bary barz
#add bar b
#create zoo bar
#create zoo2 zoo
#create zoo3 zoo2
#add bary b
#create doo zoo
#get zoo b

#Ответ
#bar