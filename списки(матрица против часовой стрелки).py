number = int(input())
joblist = [[0 for elem in range(number)] for row in range(number)] #создание матрицы размером n * n согласно введенному числу
row, elem = 0, 0 # присвоение начальному значению строки и элемента т.к. использую цикл while а не for
elem_num = number + 1 # подвижное значение для элемента что бы корректироваться после круга
row_num = 0   # подвижное в будущем значение для строки что бы корректироваться после круга
enumerator = 1 # счетчик искомых числен которые будут заполнять матрицу
line1 = 0  # объявление линий заполнения верхняя потом правая и нижняя и затем правая. Стартовые значения меняются так как рамки сужаются.
line2, line3 = 1, 1
line4 = 2
linecontrol = number - 2
while enumerator != number * number + 1: #цикл который действует пока счетчик не превысит квадрат числа т.к. форма квадрата + 1 для последней итерации
    if number > line1: # верх -  сравнение количества элементов с счетчиком интераций в данной линии
        joblist[row][elem] = enumerator # добавляю число счетчика в матрицу
        row = row_num                        #
        elem += 1                       #
        enumerator += 1                 #
        line1 += 1                      # добавляю значение к счетчику строки что бы интераций в строке было столько же сколько элементов в ней
    elif number > line2: # право
        row += 1
        elem = number - elem_num
        joblist[row][elem] = enumerator
        enumerator += 1
        line2 += 1
    elif number > line3: # низ
        row = number - row_num - 1
        elem -= 1
        joblist[row][elem] = enumerator
        enumerator += 1
        line3 += 1
    elif number > line4: # лево
        row -= 1
        joblist[row][elem] = enumerator
        enumerator += 1
        line4 += 1
    else:
        line1 -= linecontrol
        linecontrol -= 1
        line2 -= linecontrol
        line3 -= linecontrol
        linecontrol -= 1
        line4 -= linecontrol
        elem = elem_num - number
        elem_num += 1
        row_num += 1
for row in joblist:
    print(' '.join([str(elem) for elem in row]))

#Возможен такой вывод:
#for i in range(len(joblist)):
#    for j in range(len(joblist[i])):
#        finishlist.append(joblist[i][j])
#    print(*finishlist, end = ' ')
#    finishlist = []
#    print()

#Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, 
#как показано в примере (здесь n=5):
#Sample Input:
#5
#Sample Output:
#1 2 3 4 5
#16 17 18 19 6
#15 24 25 20 7
#14 23 22 21 8
#13 12 11 10 9
