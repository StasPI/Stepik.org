x = int(input())

q = x // 1000
q1 = q // 100
qq = q % 100
q2 = qq // 10
q3 = qq % 10
qx = q1 + q2 + q3

w = x % 1000
w1 = w // 100
ww = w % 100
w2 = ww // 10
w3 = ww % 10
wx = w1 + w2 + w3

if qx == wx:
    print('Счастливый')
else:
    print('Обычный')