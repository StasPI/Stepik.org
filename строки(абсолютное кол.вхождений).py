'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
Выведите одно число – количество вхождений строки t в строку s.
Пример:
s = "abababa"
t = "aba"
Вхождения строки t в строку s:
abababa
abababa
abababa
Sample Input 1:
abababa
aba
Sample Output 1:
3
Sample Input 2:
abababa
abc
Sample Output 2:
0
Sample Input 3:
abc
abc
Sample Output 3:
1
Sample Input 4:
aaaaa
a
Sample Output 4:
5
'''


s, t = str(input()), str(input())

step = 0
count = 0
for element in range(len(s)):
    if s.count(t, step) > 0:
        step = s.index(t, step)
        step += 1
        count += 1
print(count)
