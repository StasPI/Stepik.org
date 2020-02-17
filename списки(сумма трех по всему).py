firstlist = [int(i) for i in input().split()]

finallist = []

if len(firstlist) == 1:
   print(*firstlist)
elif len(firstlist) > 1:
    firstlist.append(firstlist[0])
    firstlist.insert(0, firstlist[-2])
    for i in range(len(firstlist) - 2):
        a = firstlist[0:3]
        del a[1]
        del firstlist[0]
        b = sum(a)
        finallist.append(b)

print(*finallist)

#Напишите программу, на вход которой подаётся список чисел одной строкой. Программа должна для каждого элемента этого 
#списка вывести сумму двух его соседей. Для элементов списка, являющихся крайними, одним из соседей считается элемент, 
#находящий на противоположном конце этого списка. Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается 
#список "13 6 9 15 7" (без кавычек).
#Если на вход пришло только одно число, надо вывести его же.
#Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.
#Sample Input 1:
#1 3 5 6 10
#Sample Output 1:
#13 6 9 15 7
#Sample Input 2:
#10
#Sample Output 2:
#10