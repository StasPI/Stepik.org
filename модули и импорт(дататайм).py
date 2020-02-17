'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.
Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты 
date пройдет число дней, равное days.
Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате.
Sample Input 1:
2016 4 20
14
Sample Output 1:
2016 5 4
Sample Input 2:
2016 2 20
9
Sample Output 2:
2016 2 29
Sample Input 3:
2015 12 31
1
Sample Output 3:
2016 1 1
'''

from datetime import timedelta, date

start_date = [int(number) for number in input().split()]
up_date = int(input())

start_datetime = date(start_date[0], start_date[1], start_date[2])
up_datetime = timedelta(days=up_date)
finish_date = start_datetime + up_datetime
print(finish_date.year, finish_date.month, finish_date.day)

# import datetime
# start_date = [int(number) for number in input().split()]
# up_date = int(input())

# start_datetime = datetime.date(start_date[0], start_date[1], start_date[2])
# up_datetime = datetime.timedelta(days=up_date)
# finish_date = str(start_datetime + up_datetime)
# finish_date = finish_date.split('-')
# for element in finish_date:
#     print(int(element), end=' ')
