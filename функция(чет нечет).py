lst = [int(i) for i in input().split()]
def modify_list(lst):
    for i in range(len(lst)):
        q = 0                            #счетчик индекса т.к. при удалении значения из функции индекс перескакивает
        if lst[q] % 2 == 0:
            lst.append(int(lst[q] / 2))
            lst.remove(lst[q])
            q += 1
        else:
            lst.remove(lst[q])
            q += 1
print(modify_list(lst))          
print(lst)

#Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, 
#а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#lst = [1, 2, 3, 4, 5, 6]
#print(modify_list(lst))  # None
#print(lst)               # [1, 2, 3]
#modify_list(lst)
#print(lst)               # [1]
#lst = [10, 5, 8, 3]
#modify_list(lst)
#print(lst)               # [5, 4]
#Функция не должна осуществлять ввод / вывод информации.