lenlist = int(input())
lenlist -= 1
firstnumber = int(1)
secondlist = [1]
for element in range(lenlist - 1):
    firstnumber += 1
    for element in range(firstnumber):
        if lenlist > 0:
            secondlist.append(firstnumber)
            lenlist -= 1
print(*secondlist)

#Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).
#На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. 
#На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
#Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
#Sample Input:
#7
#Sample Output:
#1 2 2 3 3 3 4