firstlist = []
secondlist = []
finishlist = []
summa = 1
finishsumma = 0
while summa != 0:
    if summa != 0:
        firstlist = [int(i) for i in input().split()]
        secondlist.append(firstlist[0])
        summa = sum(secondlist)
        finishlist.append(firstlist[0] * firstlist[0])
        finishsumma = sum(finishlist)
print(finishsumma)

#Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, пока сумма введённых чисел не 
#будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
#Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
#В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю и выводим 
#сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.﻿
#Sample Input:
#1
#-3
#5
#-6
#-10
#13
#4
#-8
#Sample Output:
#340