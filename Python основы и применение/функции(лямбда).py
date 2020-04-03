'''
Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте». 
Но иногда, когда нужно создавать много однотипных лямбда функций, еще удобнее будет создать 
функцию, которая будет их генерировать.
Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного 
аргумента y, которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.
﻿Пример использования:
mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True
'''

#№1


def mod_checker(x, mod=0): return lambda y: y % x == mod

#№2
# mod_checker = lambda x, mod=0: lambda y: y % x == mod

#№3
# def mod_checker(x, mod=0):
#  return lambda y: y % x == mod

#№4
# def mod_checker(x, mod=0):
#   def f2(y):
#     return y % x == mod
#   return f2
