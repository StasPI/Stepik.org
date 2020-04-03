read_list = []
averag_student = []
averag_science = []
summa_student = 0
summa_science = 0
counter = 0
#прочитал, разделил элементы по знаку ";"
with open(r'A:\a.txt') as inf:
    for line in inf:
        line = line.strip().split(';')
        read_list.append(line)
#вычислил среднее по каждому студенту. по окончанию цикла закинул последнее значение в список
for line in read_list:
    averag_student.append(summa_student / len(line[1:]))
    summa_student = 0
    for number in line[1:]:
        summa_student += int(number)
averag_student.append(summa_student / len(line[1:]))
del averag_student[0]
#вычислил среднее значение по каждому предмету. по окончанию цикла закинул последнее значение в список
while counter < len(line[1:]):
    counter += 1
    averag_science.append(summa_science / len(read_list))
    summa_science = 0
    for column in read_list:
        summa_science += int(column[counter])
averag_science.append(summa_science / len(read_list))
del averag_science[0]
#первым циклом записал среднее студентов с переносом строки, вторым записал среднее по предмету через пробел
with open (r'A:\b.txt', 'r+') as ouf:
    for student in averag_student:
        ouf.write(str(student))
        ouf.write('\n')
    for science in averag_science:
        ouf.write(str(science))
        ouf.write(' ')

#Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в 
#каждой строке записана следующая информация:
#Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
#Поля внутри строки разделены точкой с запятой, оценки — целые числа.
#Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит 
#его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
#Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике
#и русскому языку по всем абитуриентам.
#В качестве ответа на задание прикрепите полученный файл со средними оценками.
#Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#print('First;Second-1 Second-2;Third'.split(';'))
## ['First', 'Second-1 Second-2', 'Third']
#Sample Input:
#Петров;85;92;78
#Сидоров;100;88;94
#Иванов;58;72;85
#Sample Output:
#85.0
#94.0
#71.666666667
#81.0 84.0 85.666666667
#У вас есть неограниченное число попыток.
#Время одной попытки: 5 mins