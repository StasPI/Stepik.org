startlist = [int(i) for i in input().split()]
firstnumber = int(input())
finishlist = []
controllist = []
a = -1
for i in startlist:
    a += 1
    if i == firstnumber:
        finishlist.append(a)
if finishlist == controllist:
    print('Отсутствует')
else:
    print(*finishlist)

#Напишите программу, которая считывает список чисел lst из первой строки и число x из второй строки, которая выводит все позиции, 
#на которых встречается число x в переданном списке lst.
#Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
#Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
#Sample Input 1:
#5 8 2 7 8 8 2 4
#8
#Sample Output 1:
#1 4 5
#Sample Input 2:
#5 8 2 7 8 8 2 4
#10
#Sample Output 2:
#Отсутствует