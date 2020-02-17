x = int(input())
if ((x % 10) == 1 and x != 11) and (x % 100) != 11:
    print(x, 'программист')
elif (x % 100) != 12 and (x % 100) != 13 and (x % 100) != 14 and (2 <= x <= 4 or (x % 10) == 2 or (x % 10) == 3 or (x % 10) == 4):
    print(x, 'программиста')
else:
    print(x, 'программистов')

